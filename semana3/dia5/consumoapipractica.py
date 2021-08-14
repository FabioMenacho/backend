import requests
import json

URL = 'https://fmenachopracticaapi.herokuapp.com'

headers = {'Content-type': 'application/json'}
body = {'nombre':'Consuelo Menacho','email':'consuelo@gmail.com'}
r = requests.post(URL + '/setAlumno', data = json.dumps(body), headers = headers)
print(r)

g = requests.get(URL + '/alumnos')
print(g.text)