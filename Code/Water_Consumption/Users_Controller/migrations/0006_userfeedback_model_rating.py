# Generated by Django 2.0.5 on 2019-02-02 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users_Controller', '0005_auto_20190201_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfeedback_model',
            name='rating',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
