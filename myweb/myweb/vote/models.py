from django.db import models


# Create your models here.

class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50)
    create_date = models.DateTimeField(max_length=6)
    end_date = models.DateTimeField(max_length=6)
    create_user = models.CharField(max_length=16)

    class Meta:
        db_table = "vote"


class Vote_user(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = "vote_user"
