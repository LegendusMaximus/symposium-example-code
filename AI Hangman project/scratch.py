import requests

# url = 'https://hangmangamerestapi20190131031658.azurewebsites.net/api/'
url = 'http://localhost:10769/api/'

# response = requests.get(url+'users/')
# response = requests.post(url+'users/', params = {'value':'hallo'})
# headers = {'Content-type': 'text/plain'}
# headers = {'Content-type': 'application/json'}
# headers = {'Content-type' : 'application/x-www-form-urlencoded'}
# response = requests.post(url+'users/', headers=headers, data="{'Username':'TestUserNumber1', 'Email':'testuser1@nowhere.com', 'PasswordHash':45}")
# response = requests.post(url+'users/', data = {'Username':'TestUserNumber1', 'Email':'testuser1@nowhere.com', 'PasswordHash':45})
# response = requests.post(url+'users/', json = {'Username':'TestUserNumber1', 'Email':'testuser1@nowhere.com', 'PasswordHash':45})
response = requests.post(url+'users/', data = "{'Username':'TestUserNumber1', 'Email':'testuser1@nowhere.com', 'PasswordHash':45}")
# response = requests.post(url+'users/', data = 'hallo')
print(response)

