from django.db import models

# Create your models here.
class User(models.Model):
   first_name = models.CharField(max_length = 50)
   last_name = models.CharField(max_length = 50)     
   email = models.EmailField(max_length = 79, unique = True)
# class Meta:
#         app_label = 'first_app' 