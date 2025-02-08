import requests

# Request Forms
r = requests.get('http:// /')
r = requests.head('http:// /get')
r = requests.post('http:// /post',data={'key': 'value'})