from django.db import models


class Save(models.Model):
    save_file = models.FileField(upload_to='saves/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Save {self.id}"
