from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    duration = models.IntegerField()
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title