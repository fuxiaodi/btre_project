from django.db import models

# Create your models here.
from django.db import models

class MyModel(models.Model):
    # 其他字段...
    shapefile = models.FileField(upload_to='shapefiles/')
