import requests

#res = requests.delete(url, **kwargs)

params = {
  'status': 'available'
}

headers = {
  'accept': 'application/json',
}

data = {
  "id": 0,
  "username": "bibaboba",
  "firstName": "Biba",
  "lastName": "Boba",
  "email": "biba@bobamail.ru",
  "password": "Bob@task12",
  "phone": "89009009090",
  "userStatus": 0
}

res1 = requests.delete(f'https://petstore.swagger.io/v2/user/bibaboba', headers=headers, json=data)
print(res1.status_code)
print(res1.text)
print(res1.json())
print(type(res1.json()))