from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    specialization = models.CharField(max_length=255)
    tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='universities/', null=True, blank=True)  # Поле для изображения
    description = models.TextField(max_length=300)
    def __str__(self):
        return self.name
