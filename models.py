from django.db import models

class AgendaGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class AgendaItem(models.Model):
    group = models.ForeignKey(AgendaGroup, on_delete=models.CASCADE, related_name='items')
    time = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.time} - {self.description}"
