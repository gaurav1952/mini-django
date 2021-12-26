from django.db import models

# Create your models here.
class sotasks(models.Model):
    hellotask= models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.hellotask

