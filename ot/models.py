from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    id = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, )
    descriptions = models.TextField()
    completed = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
