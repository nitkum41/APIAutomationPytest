from http.client import responses

import requests,json

url = 'https://reqres.in/'

# param ={
#     'page':1,
#     'per_page':10
# }

head = {
    'Content-Type':'application/json'
}

data_file = open('users.json')
data = json.load(data_file)


response = requests.post(url=url+'api/users',json=data,headers=head)

print(response.status_code)
data = response.json()

print(len(data))