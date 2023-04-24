from django.db import models

# Create your models here.


class MyModel(models.Model):
   
    image_url = models.FileField(upload_to="uploads/")



from django.db import models


class User_Profile(models.Model):
    fname = models.CharField(max_length=200)
    display_picture = models.FileField()

    def __str__(self):
        return self.fname
    


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    nameofimage = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='store')
    objects = models.Manager

    class Meta:
        db_table = "table"