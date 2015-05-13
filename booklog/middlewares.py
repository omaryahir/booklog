import django.conf as conf
import os.path


class SelectDB(object):

    def process_request(self, request):
        print "inicio middleware"
        print os.path.isfile("booklog/database.txt")
        file_database = open("booklog/database.txt", "r")
        database = file_database.read(10)
        print database
        file_database.close()
        conf.settings.DATABASES['default']['NAME'] = database
        #conf.settings.SECRET_KEY = 'hola'
        #print conf.settings.SECRET_KEY
        print "Entro siempre a seleccionar la base"
