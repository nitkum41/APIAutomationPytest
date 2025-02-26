import uuid

import pytest

from utils.api_client import APIClient

@pytest.fixture(scope="module")
def api_client():
    return APIClient()

def test_get_users(api_client):
    response = api_client.get("users")
    print(response.json())
    assert response.status_code==200
    assert len(response.json()) > 0


def test_create_users(api_client,load_user_data):
    users_data= load_user_data["new_user"]  ##from the fixture

    unique_email = f"{uuid.uuid4().hex[:8]}gmail.com"
    print(unique_email)
    users_data["email"]=unique_email

    response = api_client.post("users",users_data)
    print(response.json())
    assert response.status_code==201
    assert response.json()['name']=='Rajiv1'

    response = api_client.get("users/10")
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'Clementina DuBuque'
    assert response.json()['username'] == 'Moriah.Stanton'

def test_update_users(api_client):
    users_data={
        'name': 'Rajiv1',
        'username':'rajiv1123',
        'email':'rjv1@gmail.com'
    }
    response = api_client.put("users/1",users_data)
    print(response.json())
    assert response.status_code==200
    assert response.json()['name']=='Rajiv1'

def test_delete_users(api_client):

    response = api_client.delete("users/1")
    print(response.json())
    assert response.status_code==200
