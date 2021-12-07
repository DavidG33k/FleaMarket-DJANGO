import pytest
from mixer.backend.django import mixer
from django.core.exceptions import ValidationError


# name
def test_item_name_of_length_more_than_30(db):
    item = mixer.blend('FleaMarketItem.Item', name='A'*31)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_name_length_equal_to_zero(db):
    item = mixer.blend('FleaMarketItem.Item', name='')
    with pytest.raises(ValidationError):
        item.full_clean()


# description
def test_item_description_of_length_more_than_200(db):
    item = mixer.blend('FleaMarketItem.Item', description='A'*200)
    with pytest.raises(ValidationError):
        item.full_clean()


# condition
def test_item_condition_different_enum_value(db):
    item = mixer.blend('FleaMarketItem.Item', condition='SBAGLIATO')
    with pytest.raises(ValidationError):
        item.full_clean()
