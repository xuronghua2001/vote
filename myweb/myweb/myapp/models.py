from django.db import models

# Create your models here.

class Stu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    age = models.SmallIntegerField()
    gen = models.CharField(max_length=1)
    classid = models.CharField(max_length=8)

    def __str__(self):
        return "{0}:{1}:{2}:{3}:{4}".format(self.id,self.name,self.age,self.gen,self.classid)
    #myapp_stu
    class Meta:
        db_table = "stu"

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    age = models.SmallIntegerField()
    telephone = models.CharField(max_length=11)
    date = models.DateField()

    def __str__(self):
        return "{0}:{1}".format(self.name,self.telephone)
    #myapp_stu
    class Meta:
        db_table = "user"



class myapp_users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    addtime = models.DateTimeField()

    def __str__(self):
        return "{0}:{1}".format(self.name,self.phone)
    #myapp_stu
    class Meta:
        db_table = "myapp_users"