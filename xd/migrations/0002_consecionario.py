# Generated by Django 4.0.1 on 2022-01-12 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xd', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consecionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carros', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xd.carros')),
            ],
        ),
    ]
