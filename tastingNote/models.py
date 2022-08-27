from django.db import models


# Create your models here.
class Imagemeta(models.Model):
    id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(db_column="datetime")
    image_file_name = models.CharField(db_column="image_file_name", max_length=200)
