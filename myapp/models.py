from datetime import datetime
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class post(models.Model):
    title= models.CharField(max_length=100)
    body= RichTextField(blank= True, null= True)
    created_at= models.DateTimeField(default= datetime.now, blank= True)

    def __str__(self):
        return self.title