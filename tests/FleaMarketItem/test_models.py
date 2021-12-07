import pytest
from mixer.backend.django import mixer
from django.core.exceptions import ValidationError

#name, description, condition, brand
def test_item_name_of_length_25_raises_exception(db):
    item = mixer.blend('FleaMarketItem.Item',name='A'*26)
    with pytest.raises(ValidationError) as err:
        item.full_clean()
    assert 'at most 25 characters' in '\n'.join(err.value.messages)

def test_item_name_of_less_than_1_raises_exception(db):
    item = mixer.blend('FleaMarketItem.Item',name='')
    with pytest.raises(ValidationError) as err:
        item.full_clean()
    assert 'no empty paramter name' in '\n'.join(err.value.messages)

def test_item_name_forbidden_characters_raises_exception(db):
    item = mixer.blend('FleaMarketItem.Item',name='<')
    with pytest.raises(ValidationError) as err:
        item.full_clean()
    assert 'not special character in prm name' in '\n'.join(err.value.messages)


