from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from FleaMarketItem.validators import validate_price
from django.utils.translation import gettext_lazy as _


# condition enum definition
def condition_status():
    choices = ['AS_NEW', 'GOOD_CONDITION', 'ACCEPTABLE_CONDITION']
    return [(i, choices[i]) for i in range(len(choices))]


class Item(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=30, validators=[RegexValidator(r'^[A-Za-z0-9]+$')])
    description = models.TextField(blank=True, max_length=200, validators=[RegexValidator(r'^[A-Za-z0-9\(\)\!\,\è\:\;\'\"\. ]*$')])
    condition = models.IntegerField(choices=condition_status())
    brand = models.CharField(max_length=20, validators=[RegexValidator(r'^[A-Za-z\_\-\(\)]+$')])
    price = models.IntegerField(validators=[validate_price])
    category = models.CharField(max_length=30, validators=[RegexValidator(r'^[A-Za-z\_\-\(\) ]+$')])

    def __str__(self) -> str:
        return "Utente: " + str(self.user) + " --> Item_name " + self.name

