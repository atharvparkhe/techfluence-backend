# Generated by Django 4.0.3 on 2022-04-21 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_teammodel_size'),
        ('app', '0003_alter_teameventmodel_team_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soloeventmodel',
            name='organiser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.organisersmodel'),
        ),
        migrations.AlterField(
            model_name='teameventmodel',
            name='organiser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.organisersmodel'),
        ),
    ]
