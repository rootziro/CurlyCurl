import requests

# Request Forms
r = requests.get('http:// /')
r = requests.head('http:// /get')
r = requests.post('http:// /post',data={'key': 'value'})
r = requests.options('http:// /get')

# Passing Parameters

payload = {'key1', 'value1', 'key2','value2'} # Please input actual value pairs, for these are just examples
r.requests.get('http:// /get', param = payload)
print(r.url)

# Incase URL value is none, pass with list of items
payload = {'key1', 'value1', 'key2', ['value2','value3']}

# Response Method

r = requests.get('http:// /page')
r.text()

# Find encoding Requests is utilizing
r = r.encoding()

# Change encoding if nesessary 

r.encoding = ''