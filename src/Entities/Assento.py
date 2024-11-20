from Entities.BaseModel import *
from Entities.Classe import *
from Entities.Aeronave import *

class Assento(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    id_aeronave = ForeignKeyField(column_name='ID_AERONAVE', field='id_aeronave', model=Aeronave)
    id_assento = IntegerField(column_name='ID_ASSENTO', unique=True)
    id_classe = ForeignKeyField(column_name='ID_CLASSE', field='id_classe', model=Classe)
    localizacao = CharField(column_name='LOCALIZACAO', null=True)
    numero = CharField(column_name='NUMERO', null=True)

    class Meta:
        table_name = 'assento'
        indexes = (
            (('id_assento', 'id_classe', 'id_aeronave'), True),
        )
        primary_key = CompositeKey('id_aeronave', 'id_assento', 'id_classe')
