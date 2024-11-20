from Entities.BaseModel import *
from Entities.ReservaDeAssentoVoo import *
from Entities.TipoPagamento import *


class Pagamento(BaseModel):
    data_pagamento = DateTimeField(column_name='DATA_PAGAMENTO', null=True)
    id_pagamento = IntegerField(column_name='ID_PAGAMENTO')
    id_reserva_de_assento_voo = ForeignKeyField(column_name='ID_RESERVA_DE_ASSENTO_VOO', field='id_reserva_de_assento_voo', model=ReservaDeAssentoVoo)
    id_tipo_pagamento = ForeignKeyField(column_name='ID_TIPO_PAGAMENTO', field='id_tipo_pagamento', model=TipoPagamento)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT 'PENDENTE'")])
    valor_total = DecimalField(column_name='VALOR_TOTAL', null=True)

    class Meta:
        table_name = 'pagamento'
        indexes = (
            (('id_pagamento', 'id_reserva_de_assento_voo', 'id_tipo_pagamento'), True),
        )
        primary_key = CompositeKey('id_pagamento', 'id_reserva_de_assento_voo', 'id_tipo_pagamento')
