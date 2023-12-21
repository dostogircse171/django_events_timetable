from django.db import models

class AgendaItem(models.Model):
    time = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.time} - {self.description}"
