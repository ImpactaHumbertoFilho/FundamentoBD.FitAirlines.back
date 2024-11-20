from Entities.BaseModel import *

class Bagagem(BaseModel):
    dimensoes = CharField(column_name='DIMENSOES', null=True)
    id_bagagem = AutoField(column_name='ID_BAGAGEM')
    peso_kg = DecimalField(column_name='PESO_KG', null=True)
    preco_adicional = DecimalField(column_name='PRECO_ADICIONAL', null=True)
    tipo_bagagem = CharField(column_name='TIPO_BAGAGEM')

    class Meta:
        table_name = 'bagagem'
