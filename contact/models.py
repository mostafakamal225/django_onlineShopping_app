from django.db import models

# Create your models here.
class contactdb(models.Model):
    name = models.CharField(max_length=255)
    
    email = models.TextField()
    phone= models.IntegerField()
    email = models.TextField()
    subject = models.TextField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 
