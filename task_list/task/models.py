from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    done_date = models.DateField(auto_now_add=False)
    done = models.BooleanField(default=False)
    

    def __str__(self):
        return self.text
