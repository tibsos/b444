# Generated by Django 5.0.1 on 2024-05-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_password_note_alter_password_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='password',
            name='password',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='password',
            name='username',
            field=models.TextField(blank=True, null=True),
        ),
    ]