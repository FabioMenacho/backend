import requests
import json

URL = 'https://fmenachoapi.herokuapp.com'

headers = {'Content-type': 'application/json'}
body = {'nombre':'Hilda Menacho','email':'hilda@gmail.com'}
r = requests.post(URL + '/setAlumno', data = json.dumps(body), headers = headers)
print(r)

g = requests.get(URL + '/alumnos')
print(g.text)