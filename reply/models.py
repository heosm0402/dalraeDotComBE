from django.db import models


# Create your models here.
class Reply(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(db_column="datetime")
    name = models.CharField(db_column="name", max_length=100)
    content = models.CharField(db_column="content", max_length=1000)
