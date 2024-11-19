from Entities.BaseModel import *
from Entities.Classe import *
from Entities.Voo import *

class Assento(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    id_assento = AutoField(column_name='ID_ASSENTO')
    id_classe = ForeignKeyField(column_name='ID_CLASSE', field='id_classe', model=Classe)
    id_voo = ForeignKeyField(column_name='ID_VOO', field='id_voo', model=Voo)
    localizacao = CharField(column_name='LOCALIZACAO', null=True)
    numero = CharField(column_name='NUMERO', null=True)
    ocupado = IntegerField(column_name='OCUPADO', constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'assento'
