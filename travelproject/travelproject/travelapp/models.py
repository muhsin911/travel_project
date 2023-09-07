from django.db import models

# Create your models here.
class Place(models.Model):
    Name=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='pics')
    Description=models.TextField()
    def __str__(self):
        return self.Name

class Members(models.Model):
    Name_of_person=models.CharField(max_length=100)
    Image_of_person=models.ImageField(upload_to='pics')
    Details_of_person=models.TextField()
    def __str__(self):
        return self.Name_of_person

