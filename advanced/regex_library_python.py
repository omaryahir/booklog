
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

