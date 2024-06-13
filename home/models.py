from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    image = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 




class kid(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    image = models.ImageField(upload_to='static/images/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 


class men(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    image = models.ImageField(upload_to='static/images/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 


class women(models.Model):
    name = models.CharField(max_length=255)
    catagry = models.SlugField()
    descrip = models.TextField()
    image = models.ImageField(upload_to='static/images/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 
