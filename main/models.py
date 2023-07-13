from django.db import models

# Create your models here.
class Bot(models.Model):
    name = models.CharField(max_length=150)
    username = models.CharField(max_length=150)
    bot_id = models.PositiveIntegerField()
    bot_tokken = models.CharField(max_length=1000, unique=True)

    def __str__(self) -> str:
        return self.name

class User(models.Model):
    bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    user_id = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.first_name