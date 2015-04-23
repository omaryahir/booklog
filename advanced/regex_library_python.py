# -*- coding: utf8 -*-

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


"""
Ejercicio:

a) Encontrar los números en la oración:
   L05 NUM3R0 53RAN 3L1M1NAD05.
   Posteriormente los espacios en la anterior
   por guiones bajos.

b) Obtener una lista de las palabras por cada oración
"""

#Solución a)
sinnum = re.sub(r'[0-9]','','L05 NUM3R0 53RAN 3L1M1NAD05.') 
# Otra forma es con sinnum = re.sub(r'\d','',sinnum)
conguion = re.sub(r'\s','_',sinnum)
print "sinnum %s\nconguion %s" % (sinnum,conguion)
#Salida:
#sinnum: L NUMR RAN LMNAD.
#conguion: L_NUMR_RAN_LMNAD.

#Solución b)
lista = re.findall(r'(\w+)',sinum)
# Otra forma es usando: r'[a-zA-Z]+' o también r'[^_]+
print lista
#Salida: ['L', 'NUMR', 'RAN', 'LMNAD']


"""
NOTA IMPORTANTE:

Existen símbolos como la ñ, para este fin es muy importante
utilizar el sufijo u, Ejemplo:

ur"^@([\w\-]+)$" 

"""
#Ejemplo:
string = u'españa'
re.sub(ur'ñ', u'ny', string)







