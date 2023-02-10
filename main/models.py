from django.db import models
from django.contrib.auth.models import User

class to_do_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class item(models.Model):
    todolist = models.ForeignKey(to_do_list, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
