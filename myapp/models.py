from django.db import models

class TaskModel(models.Model):
  title = models.CharField(max_length=100)
  completed = models.BooleanField(default=False)
  created_at = models.DateField(auto_now_add=True)
  
  def __str__(self):
    return self.title
