from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models


class Item(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE())
    name = models.CharField(max_length=25, validators=[RegexValidator(r'^[A-Za-z0-9 \-\_]+$')])
    description = models.TextField(blank=True,
                                   validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{1,100}$')])

