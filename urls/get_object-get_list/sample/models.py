from django.db import models

# Create your models here.

class Test(models.Model):
    text = models.CharField( max_length=300)
    true_tab = models.BooleanField(default=True)
    
    def __str__(self):
        return self.text
