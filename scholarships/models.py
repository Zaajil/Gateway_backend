from django.db import models
from django.utils import timezone

class Scholarships(models.Model):
    id = models.AutoField(primary_key=True)
    scholarship_name = models.CharField(max_length=64)
    about_scholarship = models.TextField()  
    eligibility_scholarship = models.TextField()
    amount_scholarship = models.PositiveIntegerField(default=0)  
    lastdate_scholarship = models.DateField(default=timezone.now)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('all', 'All')
    ]
    COURSE_CHOICES = [
        ('Upto 10th', 'Upto 10th'),
        ('12th', '12th'),
        ('Graduation', 'Graduation'),
        ('Postgraduate', 'Postgraduate'),
        # Add more choices as needed
    ]
    INSTITUTION_CHOICES = [
        ('Kerala', 'Kerala'),
        ('outside kerala', 'Outside Kerala'),
        ('all', 'All')
    ]
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    institution = models.CharField(max_length=20, choices=INSTITUTION_CHOICES)

    def __str__(self):
        return self.scholarship_name
