
from django.contrib import admin
from .models import Certificate
import os

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
 list_display=('user','title','uploaded_at')
 actions=['bulk_upload']

 def bulk_upload(self,request,queryset):
  pass
