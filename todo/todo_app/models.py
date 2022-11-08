from django.db import models


class Task(models.Model):  # модель бази данних
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    text = models.CharField(max_length=150)  # масимальна довжина тексту 150 символів

    def __str__(self):
        return self.text
