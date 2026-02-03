import mimetypes

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


@login_required
def dashboard(request):
 return render(request,'dashboard.html',{
  'certificates':request.user.certificates.all()
 })


@login_required
def download_certificate(request, cert_id):
    cert = get_object_or_404(
        request.user.certificates,
        id=cert_id
    )

    file_obj = cert.file
    mime_type, _ = mimetypes.guess_type(file_obj.name)

    response = HttpResponse(
        file_obj.open('rb'),
        content_type=mime_type or 'application/octet-stream'
    )

    response['Content-Disposition'] = f'attachment; filename="{file_obj.name.split("/")[-1]}"'
    return response