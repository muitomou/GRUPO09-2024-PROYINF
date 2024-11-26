# Generated by Django 5.1.2 on 2024-11-18 20:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_tag_boletinfavoritos_tagboletin'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='boletin',
            name='archivo_pdf',
            field=models.FileField(blank=True, null=True, upload_to='boletines/pdfs/'),
        ),
        migrations.AddField(
            model_name='boletin',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='boletines/images/'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ComentarioBoletin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Boletin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.boletin')),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.comentario')),
            ],
        ),
    ]