from store.models import *
from model_bakery import baker
from django.contrib.auth.models import User
from rest_framework import status
# from rest_framework.test import APIClient
import pytest


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection():
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        #arrange act assert
        
        # client = APIClient()
        response = create_collection({'title' : 'a'})
        # response = api_client.post('/store/collections/', {'title' : 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        
        
    def test_if_user_is_not_admin_returns_403(self, authenticate, create_collection):
        # client = APIClient()
        authenticate(False)
        # api_client.force_authenticate(user={})
        response = create_collection({'title' : 'a'})
        # response = api_client.post('/store/collections/', {'title' : 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN
        
    def test_if_is_invalid_returns_404(self, authenticate, create_collection):
        # client = APIClient()
        authenticate()
        # api_client.force_authenticate(user=User(is_staff=True))
        response = create_collection({'title' : ''})
        # response = api_client.post('/store/collections/', {'title' : ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None
        
    def test_if_is_valid_returns_201(self,authenticate,  create_collection):
        # client = APIClient()
        authenticate()
        # api_client.force_authenticate(user=User(is_staff=True))
        response = create_collection({'title' : 'a'})  
        # response = api_client.post('/store/collections/', {'title' : 'a'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0




@pytest.mark.django_db
class TestRetriverCollection():
    def test_if_collection_exists_return_200(self, api_client):
        # Collection.objects.create(title = 'a')
        collection = baker.make(Collection)
        # baker.make(Product, collection=collection, _quantity=10) crate 10 product inside the same collection
        response = api_client.get(f'/store/collections/{collection.id}/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id' : collection.id,
            'title' : collection.title,
            'products_count' : 0
        }