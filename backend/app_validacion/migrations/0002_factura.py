# Generated by Django 5.1.6 on 2025-02-23 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_validacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('cufe', models.CharField(blank=True, max_length=100, null=True)),
                ('paginas', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('fecha_procesamiento', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
