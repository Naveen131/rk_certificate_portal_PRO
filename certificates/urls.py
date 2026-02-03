
from django.urls import path
from .views import dashboard, download_certificate

urlpatterns=[
 path('dashboard/',dashboard,name='dashboard'),
 path('download/<int:cert_id>/', download_certificate, name='download_certificate'),

]
