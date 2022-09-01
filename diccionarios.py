diccionario={
    'nombre': 'Arian',
    'edad': '20',
    'estatura': '1.65',
    'ocupacion': 'estudiante',
    'equipo favorito':'nacional',
    'libro favorito': 'el discurso del metodo',
    'comida favorita': 'pastas'
}

#accediendo de forma individual a los atributos y valores de un diccionario

#print(diccionario['nombre'])
#print(diccionario.get('edad'))

#acceder a TODOS los atributos y valores de un diccionario al mismo tiempo
#recorrer un diccionario

for clave,valor in diccionario.items():
    print(clave,valor)

#AGREGES DESDE EL CODIGO
diccionario['ya desayuno'] = 'holiii'

print(diccionario)