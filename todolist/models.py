from django.db import models
from django.contrib.auth.models import User
class taskmate(models.Model):
    manage=models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    addtask = models.CharField(max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.addtask + ":-" + str(self.done)