
from django.db import models
from django.contrib.auth.models import User

class Certificate(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='certificates')
 title=models.CharField(max_length=255)
 file=models.FileField(upload_to='certificates/')
 uploaded_at=models.DateTimeField(auto_now_add=True)
