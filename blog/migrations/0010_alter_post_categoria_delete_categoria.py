# Generated by Django 5.1.4 on 2025-01-13 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_leyenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categoria',
            field=models.CharField(choices=[('G', 'Guitarra'), ('B', 'Bajo')], default='G', max_length=1),
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
