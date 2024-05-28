from django.db import models


# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100,null=False)
    location=models.CharField(max_length=100)

    def __str__(self):
        return f"Department: {self.name} , location:{self.location}"

class Role(models.Model):
    role=models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.role

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    salary=models.IntegerField(default=0)
    dept=models.CharField(max_length=100,null=True,blank=True)
    bonus=models.IntegerField(default=0)
    role=models.IntegerField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=20,default='20')
    hire_date=models.DateField(auto_now=True)
    # username = models.CharField(max_length=150,blank=True,null = True)
    # password = models.CharField(max_length=128,blank=True,null = True)  # Storing passwords securely requires hashing, consider using Django's built-in authentication system
    # confirm_password =models.CharField(max_length=128,blank=True,null = True)


    def __str__(self):
             return f"Employee: {self.first_name,self.last_name,self.phone,self.role,self.dept,self.hire_date,self.bonus}"
    

