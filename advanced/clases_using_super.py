# -*- coding:utf8 -*-

class Padre(object):
    """docstring for Padre"""
    def __init__(self):
        super(Padre, self).__init__()
        print "Init del Padre"

    def valores(self):
        return 1

class Mama(object):
    def valores(self):
        return 2

class Hijo(Padre):
    """docstring for Hijo"""
    def __init__(self):
        super(Hijo, self).__init__()
        print "Init del Hijo"

    def valores(self):
        valores_ancestros = super(Hijo, self).valores()
        return valores_ancestros + 1


class OtroHijo(Padre, Mama):
    """docstring for OtroHijo"""
    def __init__(self):
        super(OtroHijo, self).__init__()
        print "Init del Otro Hijo"

    def valores(self):
        valores_ancestros = Mama.valores(self)
        return valores_ancestros + 1


print "--" * 5 + " Clase Padre " + "--" * 5
a = Padre()
print 
print
print "--" * 5 + " Clase Hijo " + "--" * 5
b = Hijo()
print
print
print "--" * 5 + " Clase OtroHijo " + "--" * 5
c = OtroHijo()
print 
print 

print "Padre.valores() -->", a.valores()
print "Hijo.valores() -->", b.valores()
print "OtroHijo.valores() -->", c.valores()

