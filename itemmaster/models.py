from django.db import models

class itemmaster(models.Model):
    itemcode= models.CharField(max_length=50)
    itemname= models.CharField(max_length=250)

    def _str_(self):
        return self.itemname
