from django.urls import path
from .views import upload_file, upload_pdfs, listar_facturas

urlpatterns = [
    path("upload/", upload_file, name="upload_file"),
    path("upload-pdf/", upload_pdfs , name="eupload_pdfs"),
    path('listar-facturas/', listar_facturas, name='listar_facturas'),
]