from django.db import models

class Note(models.Model):
    text = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    
    
    
# and write this in terminal address -->>   python manage.py makemigrations notes



# than write terminal -->>                  python manage.py migrate
