from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from FleaMarketItem.validators import validate_price
from django.utils.translation import gettext_lazy as _


# condition enum definition
class ConditionStatus(models.TextChoices):
    AS_NEW = 'AN', _('AS_NEW')
    GOOD_CONDITION = 'GC', _('GOOD_CONDITION')
    ACCEPTABLE_CONDITION = 'AC', _('ACCEPTABLE_CONDITION')


class Item(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=30, validators=[RegexValidator(r'^[A-Za-z0-9 \-\_]+$')])
    description = models.TextField(blank=True, max_length=200, validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{1,200}$')])
    condition = models.CharField(ConditionStatus.choices, max_length=30)
    brand = models.CharField(max_length=20, validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{1,20}$')])
    price = models.IntegerField(validators=[validate_price])
    category = models.CharField(max_length=30, validators=[RegexValidator(r'^[A-Za-z0-9\_\-\(\)\.\,\;\&\:\=\è\'\"\! ]{1,30}$')])

    def __str__(self) -> str:
        return str(self.user) + " - " + self.name

