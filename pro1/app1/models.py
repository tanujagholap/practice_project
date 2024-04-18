from django.core import validators
from django.db import models


class Create(models.Model):
    choice2 = [('male', 'MALE'), ('female', 'FEMALE')]
    choice1 = (('YES', 'yes'), ('NO', 'no'))
    f_name = models.CharField(max_length=20)
    s_name = models.CharField(max_length=20)
    mobile_no = models.CharField(max_length=20, validators=[validators.RegexValidator('[7-9]{1}+[0-9]{9}')])
    rooms = models.IntegerField()
    ac = models.CharField(max_length=10, choices=choice1)
    gender = models.CharField(max_length=10, choices=choice2)

