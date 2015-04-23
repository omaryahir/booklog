
# Cargar la librería
import re
regex = re.compile(r"^@([\w\-]+)$")

# Utilizando el método match
regex.match("@velazcoMtz")

"""
Si match lo encuentra regresa un objeto 
en caso contrario regresa None
"""
cuenta = "@velazcoMtz" 
if regex.match(cuenta):
    print "Es una cuenta valida"
else:
    print "Es una cuenta invalida"

# El método match
regex2 = re.compile(r"me")
regex2.search("Mi mamá me mima")

"""
Método find:
Regresa [velazcoMtz] debido al 
uso de los capturadores ()
"""
# Ejemplo 1
print regex.findall("@velazcoMtz")

# Ejemplo 2
prueba = re.compile(r"m")
print prueba.findall("mi mama me mima")
# Resultado: ['m', 'm', 'm', 'm', 'm', 'm']

"""
Usando sub para sustituir carácteres
"""
re.sub(r'a', 'e', 'mi mama me mima') 
# Salida: 'mi meme me mime'


"""
Usando groupdict
"""

user_name = re.match(r'^@(?P<user_name>[\w\-]+)$',"@velazcoMtz")
print user_name.groupdict() 
#Salida: {'user_name': 'velazcoMtz}


"""
Ejercicio cardinales:
Detectar Norte, norte, Sur, sur, Este, 
este, Oeste, oeste 
"""

re.findall(r'([n|N]orte|[s|S]ur|[e|E]ste|[o|O]este])', "El oeste esta a 1 lux del norte y dos del Sur cerca del oeste")

#Salida: ['oeste', 'norte', 'Sur', 'oeste']








