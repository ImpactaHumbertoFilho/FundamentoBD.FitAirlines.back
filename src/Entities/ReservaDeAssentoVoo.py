from Entities.BaseModel import *

from Entities.Assento import Assento
from Entities.Passageiro import Passageiro
from Entities.Voo import Voo

class ReservaDeAssentoVoo(BaseModel):
    data = DateField(column_name='DATA', null=True)
    id_assento = ForeignKeyField(column_name='ID_ASSENTO', field='id_assento', model=Assento)
    id_passageiro = ForeignKeyField(column_name='ID_PASSAGEIRO', field='id_passageiro', model=Passageiro)
    id_reserva_de_assento_voo = IntegerField(column_name='ID_RESERVA_DE_ASSENTO_VOO')
    id_voo = ForeignKeyField(column_name='ID_VOO', field='id_voo', model=Voo)
    valor_total = DecimalField(column_name='VALOR_TOTAL', null=True)

    class Meta:
        table_name = 'reserva_de_assento_voo'
        indexes = (
            (('id_reserva_de_assento_voo', 'id_voo', 'id_assento', 'id_passageiro'), True),
        )
        primary_key = CompositeKey('id_assento', 'id_passageiro', 'id_reserva_de_assento_voo', 'id_voo')
