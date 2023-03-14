from django.db import models
from datetime import date

# Create your models here.
class Master(models.Model):
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=20)
    IsActive=models.BooleanField(default=False)

    class Meta:
        db_table='Master'
    
    def __str__(self) -> str:
        return self.Email
    
Gender_Choices=(
    ('m','male'),
    ('f','female'),
)
    
class User_Profile(models.Model):
    Master= models.ForeignKey(Master, on_delete=models.CASCADE)

    Image=models.FileField(upload_to='profiles/',default='default_icon.png')
    Full_Name=models.CharField(max_length=25)
    Gender=models.CharField(max_length=5,choices=Gender_Choices,default=str())
    BirthDate=models.DateField(default='2022-08-25')
    Mobile=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)

    class Meta:
        db_table="User_Profile"
    
    def __str__(self)->str:
        return self.Full_Name
