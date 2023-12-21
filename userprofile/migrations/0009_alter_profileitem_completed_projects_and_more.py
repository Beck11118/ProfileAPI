# Generated by Django 4.2.7 on 2023-12-21 07:21

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0008_skill_pic_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileitem',
            name='completed_projects',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='profileitem',
            name='countrywise_projects',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='profileitem',
            name='logo',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='logos'),
        ),
        migrations.AlterField(
            model_name='profileitem',
            name='years_of_experience',
            field=models.PositiveIntegerField(),
        ),
    ]
