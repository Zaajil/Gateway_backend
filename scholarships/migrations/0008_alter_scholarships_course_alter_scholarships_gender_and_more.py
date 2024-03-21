# Generated by Django 5.0.1 on 2024-03-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0007_alter_scholarships_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarships',
            name='course',
            field=models.CharField(choices=[('10th', '10th'), ('12th', '12th'), ('UG', 'Undergraduate'), ('PG', 'Postgraduate'), ('UG/PG', 'Both Undergraduate and Postgraduate')], max_length=20),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('all', 'All')], max_length=10),
        ),
        migrations.AlterField(
            model_name='scholarships',
            name='institution',
            field=models.CharField(choices=[('kerala', 'Kerala'), ('outside_kerala', 'Outside Kerala'), ('all', 'All')], max_length=20),
        ),
    ]
