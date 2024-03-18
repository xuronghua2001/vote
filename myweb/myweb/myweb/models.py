from django.db import models

# Create your models here.

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
        app_label = 'myweb'
