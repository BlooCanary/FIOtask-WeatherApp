from django.db import models

#location class to hold weather information
class Location(models.Model):
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=5)
    temperature = models.CharField(max_length=5)
    condition = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#custom user class; app doesn't use built-in user model
class customUser(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username
