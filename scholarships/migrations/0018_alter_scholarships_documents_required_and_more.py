# Generated by Django 5.0.1 on 2024-03-26 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0017_scholarships_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarships',
            name='documents_required',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='website',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
