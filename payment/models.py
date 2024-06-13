from django.db import models

# Create your models here.
class orderrev(models.Model):

    name = models.TextField()
   
    number= models.IntegerField()
    
    
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added'] 
