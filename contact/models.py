from django.db import models

class Profile(models.Model):
    title = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to='images/contact/', blank=True)
    body = models.TextField(null=True)
    signature = models.ImageField(upload_to='images/contact/', blank=True)

    def __str__(self):
        return self.title
