import requests

# Request Forms
r = requests.get('http://google.com/calender')
r = requests.head('http://google.com/get')
r = requests.post('http://google.com/post',data={'key': 'value'})