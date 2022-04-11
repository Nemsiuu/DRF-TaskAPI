from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Zadanie(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  title = models.TextField(
    max_length=100,
    null=False,
    blank=False
  )
  description = models.TextField(
    max_length=500,
    null=False,
    blank=False
  )

  UNDONE = 'U'
  DONE = 'D'
  STATUS_CHOICES = (
    (UNDONE, 'Undone'),
    (DONE, 'Done'),
  )

  status = models.CharField(
    max_length=1,
    choices=STATUS_CHOICES,
    default=UNDONE,
  )

  user = models.ForeignKey('auth.User',related_name='zadanie', on_delete = models.CASCADE)
  

 
  deadline = models.DateField(
    auto_now=False,
    null=False,
    blank=False
  )
  def __str__(self):
    return self.title

  class Meta:
    db_table = 'Zadania'