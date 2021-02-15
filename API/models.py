import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False, default=None, blank=False)

    def __str__(self):
        return '%s' % self.category_name

class Document(models.Model):
    document_no = models.CharField(max_length=50, null=False, blank=False, default=None)
    barcode = models.CharField(max_length=50, null=True, blank=True, default=None)
    title = models.CharField(max_length=500, null=False, blank=False, default=None)
    date_completed = models.DateField(null=False, blank=False, default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    type = models.BooleanField(blank=False, default=None)
    attachment = models.FileField(default=None, null=True, upload_to='attachment/')
    date_uploaded = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        unique_together = ['id', 'document_no']
        ordering = ['-id']

    def __str__(self):
        return '%d. %s' % (self.id, self.title)

# Delete file when not needed
@receiver(post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    if instance.attachment:
        if os.path.isfile(instance.attachment.path):
            os.remove(instance.attachment.path)