from Entities.BaseModel import *

class Itinerario(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    distancia_km = FloatField(column_name='DISTANCIA_KM', null=True)
    duracao = TimeField(column_name='DURACAO', null=True)
    paradas = CharField(column_name='PARADAS', null=True)
    id_itinerario = AutoField(column_name='ID_ITINERARIO')

    class Meta:
        table_name = 'itinerario'
