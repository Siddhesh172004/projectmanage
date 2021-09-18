from django.db import models
from django.utils import timezone

# Create your models here.


# shop Content  are  here.
class Contact(models.Model):
    course_id=models.AutoField
    Name=models.CharField(max_length=25)
    Email=models.CharField(max_length=50)
    Tel=models.IntegerField()
    Image = models.ImageField(upload_to="contact\images",default="contact\images\shoe.jpg")
    pub_date = models.DateField(default=timezone.now)
    Desc=models.CharField(max_length=500)
    # name=models.CharField(max_length=25)

    def __str__(self):
        return self.Name
