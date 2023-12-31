# Generated by Django 4.1.4 on 2023-08-16 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ministries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Minister_name_or_title', models.CharField(max_length=250)),
                ('Minister_content', models.TextField()),
                ('Minister_img', models.ImageField(upload_to='imag/')),
                ('Minister_publish_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-Minister_publish_date'],
            },
        ),
        migrations.CreateModel(
            name='Pastors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastor_name', models.CharField(max_length=250)),
                ('pastor_img', models.ImageField(upload_to='image/')),
                ('pastor_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=250)),
                ('event_content', models.TextField()),
                ('event_img', models.ImageField(upload_to='event_img/')),
                ('slug', models.SlugField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChurchActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
