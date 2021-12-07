import pytest
from mixer.backend.django import mixer
from django.core.exceptions import ValidationError


# name
def test_item_name_of_length_31_raises_exception(db):
    item = mixer.blend('FleaMarketItem.Item', name='A'*31)
    with pytest.raises(ValidationError) as err:
        item.full_clean()


def test_item__name_only_blank_characters_raises_exception(db):
    shopping_list_item = mixer.blend('item_shopping_list.ShoppingListItem', name='.', category='Smartphone',
                                     description='ciao', quantity=1)
    with pytest.raises(ValidationError):
        shopping_list_item.full_clean()

