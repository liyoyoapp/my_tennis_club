from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='First Name')
    last_name = models.CharField(max_length=100, verbose_name='Last Name')
    phone_number = models.IntegerField(null=True)

    #admin page Member object (1) to the string below
    def __str__(self):
        return f'{self.first_name} -  {self.last_name}'

    #super save function: add extra words when saving
    def save(self,*args,**kwargs):
        self.first_name = f"Mr./Ms.{self.first_name}"
        super().save(*args,**kwargs)
