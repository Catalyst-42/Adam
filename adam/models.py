from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Save(models.Model):
    id = models.CharField(max_length=36, primary_key=True)
    file = models.FileField(upload_to="saves/")
    name = models.CharField(max_length=36, blank=True)

    def __str__(self):
        return self.id


@receiver(post_delete, sender=Save)
def delete_save_file(sender, instance, **kwargs):
    if instance.file:
        instance.file.delete(save=False)
