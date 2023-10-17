from django.db import models

# Create your models here.
class Student(models.Model):
    projectname = models.CharField(max_length=100)
    username = models.CharField(max_length=120)
    workdescription = models.TextField(max_length=50)
    startdate = models.DateField()
    enddate = models.DateField()
    workhours = models.CharField(max_length=10)

    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.projectname
    
    