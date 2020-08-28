from django.db import models
#models module from django.db contains base class
#called model that we need to ingerit from for each model that we define. 

#create a class called Pet, and make it inherit from models.Model
class Pet(models.Model):
    SEX_CHOICES = [('M','Male'), ('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True) 
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
