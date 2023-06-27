from django.db import models

# Create your models here.
CHOICES = (("PDF","PDF"),("IMAGE","IMAGE"),("LINK","LINK"))
class User(models.Model):
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length = 50)

class Hacka(models.Model):
    Title = models.CharField(max_length = 50)
    Description = models.TextField()
    BackGround_Image = models.ImageField(upload_to = "images")
    Hackathon_Image = models.ImageField(upload_to = "images")
    Type = models.CharField(max_length = 50,choices = CHOICES, default = "LINK")
    Start_date = models.DateField()
    End_date = models.DateField()
    Reward_Prize = models.IntegerField()
    review_user = models.ForeignKey(User,on_delete = models.CASCADE)
