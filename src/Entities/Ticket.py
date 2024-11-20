from Entities.BaseModel import *
from Entities.ReservaDeAssentoVoo import *

class Ticket(BaseModel):
    data_emissao = DateTimeField(column_name='DATA_EMISSAO', null=True)
    id_reserva_de_assento_voo = ForeignKeyField(column_name='ID_RESERVA_DE_ASSENTO_VOO', field='id_reserva_de_assento_voo', model=ReservaDeAssentoVoo)
    id_ticket = IntegerField(column_name='ID_TICKET', unique=True)
    preco_final = DecimalField(column_name='PRECO_FINAL', null=True)
    status = IntegerField(column_name='STATUS', null=True)

    class Meta:
        table_name = 'ticket'
        indexes = (
            (('id_ticket', 'id_reserva_de_assento_voo'), True),
        )
        primary_key = CompositeKey('id_reserva_de_assento_voo', 'id_ticket')
