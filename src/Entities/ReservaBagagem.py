from Entities.BaseModel import *
from Entities.Bagagem import Bagagem
from Entities.ReservaDeAssentoVoo import ReservaDeAssentoVoo

class ReservaBagagem(BaseModel):
    id_bagagem = ForeignKeyField(column_name='ID_BAGAGEM', field='id_bagagem', model=Bagagem)
    id_reserva_bagagem = IntegerField(column_name='ID_RESERVA_BAGAGEM')
    id_reserva_de_assento_voo = ForeignKeyField(column_name='ID_RESERVA_DE_ASSENTO_VOO', field='id_reserva_de_assento_voo', model=ReservaDeAssentoVoo)

    class Meta:
        table_name = 'reserva_bagagem'
        indexes = (
            (('id_reserva_bagagem', 'id_bagagem', 'id_reserva_de_assento_voo'), True),
        )
        primary_key = CompositeKey('id_bagagem', 'id_reserva_bagagem', 'id_reserva_de_assento_voo')
