from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class SiteUser(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    us_psw = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(defautl=True)
    date = models.DateTimeField()

    def __str__(self):
        return self.first_name + self.last_name

