from Entities.BaseModel import *

class Passageiro(BaseModel):
    cpf = CharField(column_name='CPF', null=True)
    data_nascimento = DateTimeField(column_name='DATA_NASCIMENTO', null=True)
    email = CharField(column_name='EMAIL', null=True)
    endereco = CharField(column_name='ENDERECO', null=True)
    id_passageiro = AutoField(column_name='ID_PASSAGEIRO')
    nacionalidade = CharField(column_name='NACIONALIDADE', null=True)
    nome = CharField(column_name='NOME', null=True)
    telefone = CharField(column_name='TELEFONE', null=True)

    class Meta:
        table_name = 'passageiro'
