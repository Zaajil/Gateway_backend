from django.db import models
from django.utils import timezone

class Scholarships(models.Model):
    scholarship_name = models.CharField(max_length=64)
    about_scholarship = models.TextField()  
    eligibility_scholarship = models.TextField()
    amount_scholarship = models.PositiveIntegerField(default=0)  
    lastdate_scholarship = models.DateField(default=timezone.now)

    def __str__(self):
        return self.scholarship_name
