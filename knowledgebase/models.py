# knowledgebase/models.py
from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_registered = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed

    def __str__(self):
        return self.name
