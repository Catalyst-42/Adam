from django.db import models

class Save(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    file = models.FileField(upload_to='saves/')
    name = models.CharField(max_length=36, blank=True)

    def __str__(self):
        return self.id
