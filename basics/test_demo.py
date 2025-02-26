import pytest
import requests


def test_request_validation():
    baseurl = 'https://reqres.in/'

    head = {
        'Content-Type': 'application/json'
    }

    response = requests.get(url=baseurl+'api/users/2',headers=head)

    assert response.status_code == 200