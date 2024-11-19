from Entities.BaseModel import *
from Entities.Reserva import *
from Entities.TipoPagamento import *


class Pagamento(BaseModel):
    data_pagamento = DateTimeField(column_name='DATA_PAGAMENTO')
    id_pagamento = AutoField(column_name='ID_PAGAMENTO')
    id_reserva = ForeignKeyField(column_name='ID_RESERVA', field='id_reserva', model=Reserva)
    id_tipo_pagamento = ForeignKeyField(column_name='ID_TIPO_PAGAMENTO', field='id_tipo_pagamento', model=TipoPagamento)
    status = IntegerField(column_name='STATUS')
    valor = DecimalField(column_name='VALOR')

    class Meta:
        table_name = 'pagamento'
