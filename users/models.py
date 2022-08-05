from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column="name", max_length=100)
    sex = models.CharField(db_column="sex", max_length=5)
    birth = models.DateField(db_column="birth")
