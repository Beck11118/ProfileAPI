# Generated by Django 4.2.7 on 2023-12-21 05:43

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_profileitem_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='pic',
            field=django_resized.forms.ResizedImageField(crop=None, default='skill_default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='skill'),
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('icon', models.CharField(blank=True, max_length=200, null=True)),
                ('pic', django_resized.forms.ResizedImageField(crop=None, default='socail_default.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[1920, 1080], upload_to='social')),
                ('link', models.CharField(max_length=250)),
                ('profile_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='userprofile.profileitem')),
            ],
        ),
    ]