# Generated by Django 4.0.4 on 2022-05-31 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ranking',
            name='due_date',
            field=models.DateField(auto_now=True),
        ),
    ]