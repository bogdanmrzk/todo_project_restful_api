from django.db import models


# class Board(models.Model):
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=10, default="ARCHIVED")
#
#     def __str__(self):
#         return self.status


class Task(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    text = models.CharField(max_length=150)
    # board = models.ForeignKey("Board", default=None, on_delete=models.PROTECT, null=True, related_name='boards')

    def __str__(self):
        return self.text
