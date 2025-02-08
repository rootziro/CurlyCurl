import requests

# Request Forms
r = requests.get('http:// /')
r = requests.head('http:// /get')
r = requests.post('http:// /post',data={'key': 'value'})
r = requests.options('http:// /get')

# Passing parameters

# Please do further research as to why the key value pairs was not feasble within this set(Pylance)
payload = {'key1', 'value1', 'key2', 'value2'} # set value pairs are just examples
r.requests.get('http:// /get', params=payload)
print(r.url)

