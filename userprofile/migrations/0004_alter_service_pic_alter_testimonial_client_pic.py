# Generated by Django 4.2.7 on 2023-12-20 05:40

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='service/service_default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='service'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='client_pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='testimonial/testimonial_default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='testimonial'),
        ),
    ]
