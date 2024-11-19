from Entities.BaseModel import *

class TipoAeronave(BaseModel):
    capacidade_passageiros = IntegerField(column_name='CAPACIDADE_PASSAGEIROS', null=True)
    descricao = CharField(column_name='DESCRICAO', null=True)
    fabricante = CharField(column_name='FABRICANTE', null=True)
    id_tipo_aeronave = AutoField(column_name='ID_TIPO_AERONAVE')
    nome = CharField(column_name='NOME', null=True)

    class Meta:
        table_name = 'tipo_aeronave'
