from Entities.BaseModel import *
from Entities.Reserva import *

class Ticket(BaseModel):
    data_emissao = DateTimeField(column_name='DATA_EMISSAO')
    id_reserva = ForeignKeyField(column_name='ID_RESERVA', field='id_reserva', model=Reserva)
    id_ticket = AutoField(column_name='ID_TICKET')
    preco_final = DecimalField(column_name='PRECO_FINAL')
    status = IntegerField(column_name='STATUS')

    class Meta:
        table_name = 'ticket'