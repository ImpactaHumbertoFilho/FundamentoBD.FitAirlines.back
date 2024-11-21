from Entities.BaseModel import *
from Entities.Voo import Voo

class Relatorio(BaseModel):
    clima = CharField(column_name='CLIMA', null=True)
    data = DateTimeField(column_name='DATA', null=True)
    descricao = CharField(column_name='DESCRICAO', null=True)
    desembarque = DateTimeField(column_name='DESEMBARQUE', null=True)
    embarque = DateTimeField(column_name='EMBARQUE', null=True)
    id_relatorio = IntegerField(column_name='ID_RELATORIO')
    id_voo = ForeignKeyField(column_name='ID_VOO', field='id_voo', model=Voo)
    tempo = CharField(column_name='TEMPO', null=True)

    class Meta:
        table_name = 'relatorio'
        indexes = (
            (('id_relatorio', 'id_voo'), True),
        )
        primary_key = CompositeKey('id_relatorio', 'id_voo')
