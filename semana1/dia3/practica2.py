

alumnos = [
    {
    'nombre':'Fabio Menacho Landa',
    'email':'fmenacho@uni.pe',
    'celular':'997064940'
},
    {
    'nombre':'Hilda Menacho Landa',
    'email':'hilda@uni.pe',
    'celular':'997064941'
}
    ] 
print(alumnos)

strAlumnos = ""
for a in alumnos:
        for clave,valor in a.items():
            strAlumnos += valor
            if clave != 'celular':
                strAlumnos += ','
            else:
                strAlumnos += "\n"
print(strAlumnos)