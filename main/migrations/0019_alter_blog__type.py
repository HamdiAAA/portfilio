# Generated by Django 3.2.6 on 2021-10-19 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_blog_bg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='_type',
            field=models.CharField(blank=True, choices=[('Technology', 'Technology'), ('Movies', 'Movies'), ('Gaming', 'Gaming')], max_length=100, null=True),
        ),
    ]