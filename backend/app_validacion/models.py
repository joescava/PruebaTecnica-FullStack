from django.db import models

class ArchivoSubido(models.Model):
    archivo = models.FileField(upload_to="uploads/")
    fecha_subida = models.DateTimeField(auto_now_add=True)