from Entities.BaseModel import *

class Classe(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    id_classe = AutoField(column_name='ID_CLASSE')
    nome = CharField(column_name='NOME', null=True)
    preco_adicional = DecimalField(column_name='PRECO_ADICIONAL', null=True)
    prioridade = IntegerField(column_name='PRIORIDADE', null=True)
    tipo = CharField(column_name='TIPO', null=True)

    class Meta:
        table_name = 'classe'
