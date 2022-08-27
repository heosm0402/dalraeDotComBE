from django.db import models


# Create your models here.
class Imagemeta(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(db_column="datatime")
    image_file_name = models.CharField(db_column="image_file_name", max_length=200)
