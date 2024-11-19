from Entities.BaseModel import *
from Entities.Assento import *
from Entities.Passageiro import *

class Reserva(BaseModel):
    data = DateTimeField(column_name='DATA')
    id_assento = ForeignKeyField(column_name='ID_ASSENTO', field='id_assento', model=Assento)
    id_passageiro = ForeignKeyField(column_name='ID_PASSAGEIRO', field='id_passageiro', model=Passageiro)
    id_reserva = AutoField(column_name='ID_RESERVA')
    preco = DecimalField(column_name='PRECO')
    status = IntegerField(column_name='STATUS')

    class Meta:
        table_name = 'reserva'
