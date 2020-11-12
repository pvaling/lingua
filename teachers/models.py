from django.db import models

# Create your models here.


class Teacher(models.Model):
    firstname = models.CharField(max_length=1024)
    lastname = models.CharField(max_length=1024)
    email = models.EmailField(blank=False)

    def __str__(self):
        return self.firstname + " " + self.lastname
