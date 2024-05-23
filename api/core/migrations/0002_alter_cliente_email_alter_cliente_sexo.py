# Generated by Django 5.0.6 on 2024-05-23 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')], max_length=1),
        ),
    ]
