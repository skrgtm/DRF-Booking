from django.conf import settings
from django.db import models

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = [
        ('Flat', 'Flat'),
        ('Building', 'Building'),
    ]
    POST_TYPE_CHOICES = [
        ('Rent', 'Rent'),
        ('Sell', 'Sell'),
    ]
    BHK_CHOICES = [
        ('1BHK', '1BHK'),
        ('2BHK', '2BHK'),
        ('3BHK', '3BHK'),
        ('4BHK', '4BHK'),
        ('5BHK', '5BHK'),
        ('6BHK', '6BHK'),
    ]

    title = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50, choices=PROPERTY_TYPE_CHOICES)
    location = models.CharField(max_length=255, null=True, blank=True)
    post_type = models.CharField(max_length=50, choices=POST_TYPE_CHOICES, null=True, blank=True)
    bhk_type = models.CharField(max_length=50, choices=BHK_CHOICES)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    images = models.ManyToManyField('PropertyImage', related_name='property_images')
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='properties', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.id}"
