# Generated by Django 2.2.1 on 2019-09-18 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techapp', '0002_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discription', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='image/')),
            ],
        ),
    ]
