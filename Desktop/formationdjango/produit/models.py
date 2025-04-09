from django.db import models

class produit(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
         return self.image.url
         return None 