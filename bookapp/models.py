from django.db import models

# Create your models here.
#회원
class user(models.Model):
    user_id = models.CharField(max_length=34)
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=34)
    tel = models.CharField(max_length=30)
    addr = models.TextField()
    email = models.CharField(max_length=50)
    birth = models.DateTimeField()

    def __str__(self):
        return self.id

#