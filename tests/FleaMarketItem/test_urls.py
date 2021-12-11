import json
from mixer.backend.django import mixer
import pytest
from allauth import models
from pytest_django.fixtures import admin_user
from rest_framework.test import APIClient
from rest_framework.status import HTTP_403_FORBIDDEN, HTTP_405_METHOD_NOT_ALLOWED, HTTP_200_OK, \
    HTTP_201_CREATED,HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
from django.contrib.auth import get_user_model, models


###################### path('item/', UserShowItemList.as_view()) ############
# test che fa una get per una persona non autentificata sugli item
def test_item_get_of_non_user():
    path = '/api/v1/item/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


# test che fa una get come persona autentificata sugli item
def test_item_get_of_an_authenticated_user(flea_market_items):
    path = '/api/v1/item/'
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK


# test che fa una get come admin sugli item
def test_item_get_of_the_admin(flea_market_items, admin_user):
    path = '/api/v1/item/'
    client = get_client(admin_user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action')


###################### path('item/add', UserAddItemList.as_view()) ############
# test che fa un add per una persona non autentificata sugli item
def test_item_add_of_non_user():
    path = '/api/v1/item/add/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


# test che fa un add per uno user sugli item
def test_item_user_created(flea_market_items):
    path = '/api/v1/item/add/'
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                       'condition': '1', 'brand': 'dd', 'price': '20', 'category': 'maglia'})
    assert response.status_code == HTTP_201_CREATED
# si potrebbe accorciare il data nel client.post facendo data = flea_market_items,,, MA NON FUNZIONA


# test che fa un add per uno user ma con parametri errati
def test_item_user_created_with_wrong_values(flea_market_items):
    path = '/api/v1/item/add/'
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.post(path, data={'user': flea_market_items[0].user.pk, 'name': '.', 'description': 'ddddd',
                                    'condition': '1', 'brand': 'dd', 'price': '20', 'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': '<',
                                       'condition': '1', 'brand': 'dd', 'price': '20',
                                       'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                       'condition': '.', 'brand': 'dd', 'price': '20',
                                       'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                       'condition': '1', 'brand': '!!', 'price': '20',
                                       'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.post(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                       'condition': '1', 'brand': 'dd', 'price': '-20',
                                       'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST


# test che fa un add come admin sugli item
def test_item_admin_created(flea_market_items, admin_user):
    path = '/api/v1/item/add/'
    client = get_client(admin_user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action')


###################### path('item/edit/<int:pk>/', UserEditItemList.as_view()) ############
# test che fa un edit di un item per un non utente
def test_item_edit_of_a_non_user(flea_market_items):
    path = '/api/v1/item/edit/' + str(flea_market_items[0].pk) + '/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided.')


def test_item_show_single_item_of_an_user(flea_market_items):
    path = '/api/v1/item/edit/' + str(flea_market_items[0].pk) + '/'
    client = get_client(flea_market_items[0].user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == 7

def test_item_edit_of_an_user(flea_market_items):
    path = '/api/v1/item/edit/' + str(flea_market_items[0].pk) + '/'
    client = get_client(flea_market_items[0].user)
    response = client.put(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                       'condition': '1', 'brand': 'dd', 'price': '20',
                                       'category': 'maglia'})
    assert response.status_code == HTTP_200_OK


def test_item_edit_of_an_user_with_wrong_values(flea_market_items):
    path = '/api/v1/item/edit/' + str(flea_market_items[0].pk) + '/'
    client = get_client(flea_market_items[0].user)
    response = client.put(path, data={'user': flea_market_items[0].user.pk, 'name': '.', 'description': 'ddddd',
                                       'condition': '1', 'brand': 'dd', 'price': '20',
                                       'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.put(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': '<>',
                                      'condition': '1', 'brand': 'dd', 'price': '20',
                                      'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.put(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                      'condition': '3', 'brand': 'dd', 'price': '20',
                                      'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.put(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                      'condition': '1', 'brand': '>>', 'price': '20',
                                      'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.put(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                      'condition': '1', 'brand': 'nike', 'price': '-20',
                                      'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST
    response = client.put(path, data={'user': flea_market_items[0].user.pk, 'name': 'antonio', 'description': 'ddddd',
                                      'condition': '1', 'brand': 'dd', 'price': '-20',
                                      'category': 'maglia'})
    assert response.status_code == HTTP_400_BAD_REQUEST


def test_item_delete_item_as_user(flea_market_items):
    path = '/api/v1/item/edit/' + str(flea_market_items[0].pk) + '/'
    client = get_client(flea_market_items[0].user)
    response = client.delete(path)
    assert response.status_code == HTTP_204_NO_CONTENT


def test_item_edit_of_an_admin(flea_market_items, admin_user):
    path = '/api/v1/item/edit/' + str(flea_market_items[0].pk) + '/'
    client = get_client(admin_user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action')


###################### path('users/', ModeratorShowUserList.as_view()) ############
def test_item_path_users_of_a_non_user():
    path = '/api/v1/users/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided.')


def test_item_path_users_of_an_user(users):
    path = '/api/v1/users/'
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action')


def test_item_path_users_of_an_admin(admin_user, users):
    path = '/api/v1/users/'
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(admin_user)
    client = get_client(admin_user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == len(users)


###################### path('item-moderator/', ModeratorShowItemList.as_view()) ############
def test_item_show_list_of_the_admin_as_non_authenticated_person():
    path = '/api/v1/item-moderator/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided')


def test_item_show_list_of_the_admin_as_an_user(flea_market_items):
    path = '/api/v1/item-moderator/'
    user = mixer.blend(get_user_model())
    client = get_client(user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action')


def test_item_show_list_of_the_admin_as_an_user(flea_market_items, admin_user):
    path = '/api/v1/item-moderator/'
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(admin_user)
    client = get_client(admin_user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == len(flea_market_items)


###################### path('item-moderator/edit/<int:pk>/', ModeratorEditItemList.as_view()) ############
def test_item_edit_moderator_as_non_authenticated_person(flea_market_items):
    path = '/api/v1/item-moderator/edit/' + str(flea_market_items[0].pk) + '/'
    client = get_client()
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'credentials were not provided.')


def test_item_edit_moderator_as_an_user(flea_market_items):
    path = '/api/v1/item-moderator/edit/' + str(flea_market_items[0].pk) + '/'
    client = get_client(flea_market_items[0].user)
    response = client.get(path)
    assert response.status_code == HTTP_403_FORBIDDEN
    assert contains(response, 'detail', 'You do not have permission to perform this action')


def test_item_edit_moderator_as_admin(flea_market_items, admin_user):
    path = '/api/v1/item-moderator/edit/' + str(flea_market_items[0].pk) + '/'
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(admin_user)
    client = get_client(admin_user)
    response = client.get(path)
    assert response.status_code == HTTP_200_OK
    obj = parse(response)
    assert len(obj) == 2


def test_item_edit_moderator_as_admin_with_wrong_id(flea_market_items, admin_user):
    path = '/api/v1/item-moderator/edit/' + '999' + '/'
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(admin_user)
    client = get_client(admin_user)
    response = client.get(path)
    assert response.status_code == HTTP_404_NOT_FOUND
    # assert contains(response, 'detail', 'Not Found.')


def test_item_edit_moderator_delete(flea_market_items, admin_user):
    path = '/api/v1/item-moderator/edit/' + str(flea_market_items[0].pk) + '/'
    group = mixer.blend(models.Group, name='moderator')
    group.user_set.add(admin_user)
    client = get_client(admin_user)
    response = client.delete(path)
    assert response.status_code == HTTP_204_NO_CONTENT


@pytest.fixture
def flea_market_items(db):
    return [
        mixer.blend('FleaMarketItem.Item'),
        mixer.blend('FleaMarketItem.Item'),
        mixer.blend('FleaMarketItem.Item'),
    ]

@pytest.fixture()
def users(db):
    return [
        mixer.blend(get_user_model()),
        mixer.blend(get_user_model()),
        mixer.blend(get_user_model()),
    ]

def get_client(user=None):
    res = APIClient()
    if user is not None:
        res.force_login(user)
    return res


def parse(response):
    response.render()
    content = response.content.decode()
    return json.loads(content)


def contains(response, key, value):
    obj = parse(response)
    if key not in obj:
        return False
    return value in obj[key]


