from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=100)
    is_complete = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.title


