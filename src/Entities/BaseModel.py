from peewee import *

database = MySQLDatabase('fitairlines', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': '3025'})

class BaseModel(Model):
    class Meta:
        database = database

class UnknownField(object):
    def __init__(self, *_, **__): pass
