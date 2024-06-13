from django.db import models

# Create your models here.
class aboutdb(models.Model):
    name = models.CharField(max_length=255)
    descrip = models.TextField()
    image = models.ImageField(upload_to='static/images/')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 
