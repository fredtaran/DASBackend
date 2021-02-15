from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['document_no', 'title']