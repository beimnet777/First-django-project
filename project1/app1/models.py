from django.db import models

# Create your models here.
class nums(models.Model):
  name=models.CharField(max_length=50)
  age=models.IntegerField(null=True)
  is_offer=models.BooleanField(default=False)
  image=models.ImageField('images')
  # def __init__(self,name,age,id,t):
  #   self.name=name
  #   self.age=age
  #   self.id=id
  #   self.t=t
class nums2(models.Model):
  name=models.CharField(max_length=50)
  age=models.IntegerField(null=True)
  is_offer=models.BooleanField(default=False)
  fk=models.ForeignKey(nums,null=True,on_delete=models.CASCADE)
class nums3(models.Model):
  name=models.CharField(max_length=50)
  age=models.IntegerField(null=True)
  is_offer=models.BooleanField(default=False)
  Foreignkey=models.ManyToManyField(nums)  