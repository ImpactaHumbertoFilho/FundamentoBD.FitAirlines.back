from Entities.BaseModel import *

class TipoPagamento(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    id_tipo_pagamento = AutoField(column_name='ID_TIPO_PAGAMENTO')
    tipo = CharField(column_name='TIPO', null=True)

    class Meta:
        table_name = 'tipo_pagamento'