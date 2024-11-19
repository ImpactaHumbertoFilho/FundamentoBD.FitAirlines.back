from Entities.BaseModel import *
from Entities.Aeroporto import *
from Entities.TipoAeronave import *

class Voo(BaseModel):
    assentos_disponiveis = IntegerField(column_name='ASSENTOS_DISPONIVEIS', null=True)
    chegada = DateTimeField(column_name='CHEGADA')
    codigo = CharField(column_name='CODIGO', null=True)
    duracao = TimeField(column_name='DURACAO', null=True)
    id_aeroporto_chegada = ForeignKeyField(column_name='ID_AEROPORTO_CHEGADA', field='id_aeroporto', model=Aeroporto)
    id_aeroporto_partida = ForeignKeyField(backref='aeroporto_id_aeroporto_partida_set', column_name='ID_AEROPORTO_PARTIDA', field='id_aeroporto', model=Aeroporto)
    id_tipo_aeronave = ForeignKeyField(column_name='ID_TIPO_AERONAVE', field='id_tipo_aeronave', model=TipoAeronave)
    id_voo = AutoField(column_name='ID_VOO')
    partida = DateTimeField(column_name='PARTIDA')
    status = IntegerField(column_name='STATUS')

    class Meta:
        table_name = 'voo'
