# Generated by Django 4.2.7 on 2023-12-19 06:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('tag', models.CharField(max_length=255)),
                ('pic', django_resized.forms.ResizedImageField(crop=None, default='project/project_default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='project')),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=250)),
                ('started_at', models.DateField(blank=True, null=True)),
                ('completed_at', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('profile_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='userprofile.profileitem')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=150)),
                ('client_role', models.CharField(max_length=150)),
                ('client_pic', django_resized.forms.ResizedImageField(crop=None, default='testimonial/testimonial_default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='testimonials')),
                ('company_name', models.CharField(max_length=150)),
                ('text', models.TextField()),
                ('star', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)])),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('profile_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='userprofile.profileitem')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_testimonials', to='userprofile.project')),
            ],
        ),
    ]