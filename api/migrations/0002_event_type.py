# Generated by Django 4.0.4 on 2022-05-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('arangu', 'Arangu'), ('kalolsavam', 'Kalolsavam')], max_length=30, null=True),
        ),
    ]
