from django.db import models

class Register(models.Model):
    username=models.CharField(max_length=50)
    mobile=models.CharField(max_length=12)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.username
class Imageupload(models.Model):
    name=models.CharField(max_length=20)
    image=models.ImageField(upload_to='image/')
    def __str__(self):
        return self.name
class Addpost(models.Model):
    title=models.CharField(max_length=50)
    discription=models.CharField(max_length=250)
    image=models.ImageField(upload_to='image/')