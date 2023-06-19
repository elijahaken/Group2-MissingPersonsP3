from django.db import models

# Create your models here.
  
#This is the structure of the table/inputs for your database.  
class Race(models.Model): 
    mpRace = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.mpRace
    
class Gender(models.Model): 
    mpGender = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.mpGender

class MissingPerson(models.Model):
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    age_at_missing = models.PositiveIntegerField(null=True,blank=True)
    city_of_disappearance = models.CharField(max_length=100,null=True,blank=True)
    state_of_disappearance = models.CharField(max_length=2,null=True,blank=True)
    date_of_disappearance = models.DateField(default="1999-01-01",null=True,blank=True) # type: ignore
    race = models.ForeignKey('Race',null=True,blank=True,on_delete=models.SET_NULL)
    gender = models.ForeignKey('Gender',null=True,blank=True,on_delete=models.SET_NULL)
    picture = models.ImageField(upload_to="images/",blank=True,null=True)
    

    


    

    
