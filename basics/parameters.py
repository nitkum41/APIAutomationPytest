from http.client import responses

import requests

url = 'https://gorest.co.in/public/v2/users'

param ={
    'page':1,
    'per_page':10
}

head = {
    'Content-Type':'application/json',
    'Authorization':'Bearer 57c7064a963854558945c9e6533dff5b8e090eca72463268c9ce438bd7ac5228'
}

data = {
    "name": "Tenaligg Ramakrishna",
    "gender": "male",
    "email": "tenal1iggg.ramakrishna@15ce.com",
    "status": "active"
}

# response=requests.get(url=url,params=param)

response = requests.post(url=url,json=data,headers=head)

print(response.status_code)
data = response.json()

print(len(data))