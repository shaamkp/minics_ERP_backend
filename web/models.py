from django.db import models


class Subscribe(models.Model):
    email=models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.email

class Welcome(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to="spotlight/")

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to="About/")

    def __str__(self):
        return self.title
