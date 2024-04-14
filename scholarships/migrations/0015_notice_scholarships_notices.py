# Generated by Django 5.0.1 on 2024-03-24 11:37

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0014_rename_document_required_scholarships_documents_required'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='scholarships',
            name='notices',
            field=models.ManyToManyField(blank=True, to='scholarships.notice'),
        ),
    ]
