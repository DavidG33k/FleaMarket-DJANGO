import pytest
from mixer.backend.django import mixer
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


# name
def test_item_name_of_length_more_than_30(db):
    item = mixer.blend('FleaMarketItem.Item', name='A'*31)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_name_with_not_permitted_values(db):
    item = mixer.blend('FleaMarketItem.Item', name='<script>alert(1)</script>')
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_name_of_length_equal_to_zero(db):
    item = mixer.blend('FleaMarketItem.Item', name='')
    with pytest.raises(ValidationError):
        item.full_clean()


# description
def test_item_description_of_length_more_than_200(db):
    item = mixer.blend('FleaMarketItem.Item', description='A'*200)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_description_with_not_permitted_values(db):
    item = mixer.blend('FleaMarketItem.Item', description='<script>alert(1)</script>')
    with pytest.raises(ValidationError):
        item.full_clean()


# condition
def test_item_condition_different_enum_value(db):
    item = mixer.blend('FleaMarketItem.Item', condition='3')
    with pytest.raises(ValidationError):
        item.full_clean()


# brand
def test_item_brand_of_length_more_than_20(db):
    item = mixer.blend('FleaMarketItem.Item', brand='A'*21)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_brand_of_length_equal_to_zero(db):
    item = mixer.blend('FleaMarketItem.Item', brand='')
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_brand_with_not_permitted_values(db):
    item = mixer.blend('FleaMarketItem.Item', brand='dde98d')
    with pytest.raises(ValidationError):
        item.full_clean()


# price
def test_item_price_with_negative_value(db):
    item = mixer.blend('FleaMarketItem.Item', price=-10)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_price_with_value_greater_than_threshold(db):
    item = mixer.blend('FleaMarketItem.Item', price=10000000)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_price_with_not_permitted_values(db):
    with pytest.raises(ValidationError):
        item = mixer.blend('FleaMarketItem.Item', price='ciao')
        item.full_clean()


# category
def test_item_category_of_length_more_than_30(db):
    item = mixer.blend('FleaMarketItem.Item', category='A'*31)
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_category_of_length_equal_to_zero(db):
    item = mixer.blend('FleaMarketItem.Item', category='')
    with pytest.raises(ValidationError):
        item.full_clean()


def test_item_category_with_number(db):
    item = mixer.blend('FleaMarketItem.Item', category='dde98d')
    with pytest.raises(ValidationError):
        item.full_clean()


# to string
def test_shopping_list_item_str(db):
    user = mixer.blend(get_user_model(), username='prova')
    item = mixer.blend('FleaMarketItem.Item', user=user, name='air_force')
    tostring = item.__str__()
    assert tostring == item.__str__()
