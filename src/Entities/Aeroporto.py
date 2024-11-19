from Entities.BaseModel import *

class Aeroporto(BaseModel):
    capacidade = IntegerField(column_name='CAPACIDADE', null=True)
    cidade = CharField(column_name='CIDADE', null=True)
    codigo = CharField(column_name='CODIGO', null=True)
    estado = CharField(column_name='ESTADO', null=True)
    id_aeroporto = AutoField(column_name='ID_AEROPORTO')
    nome = CharField(column_name='NOME', null=True)
    pais = CharField(column_name='PAIS', null=True)
    latitude = DecimalField(column_name='latitude')
    longitude = DecimalField(column_name='longitude')

    class Meta:
        table_name = 'aeroporto'
