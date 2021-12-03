from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from FleaMarketItem.validators import validate_price


# condition enum definition
class ConditionStatus(models.TextChoices):
    AS_NEW = "AS_NEW",
    GOOD_CONDITION = "GOOD_CONDITION"
    ACCEPTABLE_CONDITION = "ACCEPTABLE_CONDITION"


class Item(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=25, validators=[RegexValidator(r'^[A-Za-z0-9 \-\_]+$')])
    description = models.TextField(blank=True, validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{1,100}$')])
    category = models.CharField(ConditionStatus.choices, max_length=25)
    brand = models.CharField(max_length=100, validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{1,100}$')])
    price = models.IntegerField(validators=[validate_price])
    description = models.CharField(max_length=200, validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{1,100}$')])
