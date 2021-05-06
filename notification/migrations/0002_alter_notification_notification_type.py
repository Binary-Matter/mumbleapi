# Generated by Django 3.2 on 2021-05-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification_type',
            field=models.CharField(choices=[('article', 'article'), ('mumble', 'mumble'), ('discussion', 'discussion'), ('follow', 'follow')], max_length=20),
        ),
    ]