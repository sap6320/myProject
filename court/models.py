from django.db import models

# Create your models here.
class user_query(models.Model):
    user_name=models.CharField(max_length=50, default="name")
    user_email=models.EmailField(max_length=50,default="email")
    user_number=models.CharField(max_length=20,default="0")
    user_querry=models.CharField(max_length=1000,default="querry")
    def __str__(self):
        return self.user_name + " " + self.user_email

class court(models.Model):
    court_id=models.IntegerField(default="1")
    court_name=models.CharField(max_length=50,default="court")
    court_image=models.ImageField(upload_to='court/img/court_img',default="")
    court_image2=models.ImageField(upload_to='court/img/court_img',default="")
    def __str__(self):
        return self.court_name 

class booking(models.Model):
    user_id=models.IntegerField(default="1")
    court_id=models.IntegerField(default="1")
    hour=models.IntegerField(default="1")
    date=models.DateField()
    def __strt__(self):
        return str(self.user_id) + " " + str(self.court_id)
