from django.db import models

# Create your models here.
class nums:
  name:str
  age:int
  id:int
  t:bool
  def __init__(self,name,age,id,t):
    self.name=name
    self.age=age
    self.id=id
    self.t=t