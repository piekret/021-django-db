from django.db import models

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return f'{self.title} '

    def details(self):
        return f'{self.title}: {self.ingredients} {self.instructions}'