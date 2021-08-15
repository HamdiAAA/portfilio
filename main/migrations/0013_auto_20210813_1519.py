# Generated by Django 3.2.6 on 2021-08-13 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_blog_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('body', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]