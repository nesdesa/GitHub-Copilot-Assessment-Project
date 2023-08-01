from django.db import models
import uuid


class Person(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
