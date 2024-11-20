from Entities.BaseModel import *
from Entities.Aeroporto import *
from Entities.Aeronave import *

class Voo(BaseModel):
    assentos_disponiveis = IntegerField(column_name='ASSENTOS_DISPONIVEIS', null=True)
    chegada = DateTimeField(column_name='CHEGADA', null=True)
    codigo = CharField(column_name='CODIGO', null=True)
    duracao = TimeField(column_name='DURACAO', null=True)
    id_aeronave = ForeignKeyField(column_name='ID_AERONAVE', field='id_aeronave', model=Aeronave)
    id_aeroporto_chegada = ForeignKeyField(column_name='ID_AEROPORTO_CHEGADA', field='id_aeroporto', model=Aeroporto)
    id_aeroporto_partida = ForeignKeyField(backref='aeroporto_id_aeroporto_partida_set', column_name='ID_AEROPORTO_PARTIDA', field='id_aeroporto', model=Aeroporto)
    id_voo = IntegerField(column_name='ID_VOO')
    partida = DateTimeField(column_name='PARTIDA', null=True)
    preco_base = DecimalField(column_name='PRECO_BASE', null=True)
    status = CharField(column_name='STATUS', null=True)

    class Meta:
        table_name = 'voo'
        indexes = (
            (('id_voo', 'id_aeronave', 'id_aeroporto_partida', 'id_aeroporto_chegada'), True),
        )
        primary_key = CompositeKey('id_aeronave', 'id_aeroporto_chegada', 'id_aeroporto_partida', 'id_voo')
