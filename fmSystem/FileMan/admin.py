from django.contrib import admin
from .models import UploadFile

# Register your models here.
class FileAdmin(admin.ModelAdmin):
    readonly_fields=('created',)
    
admin.site.register(UploadFile)
