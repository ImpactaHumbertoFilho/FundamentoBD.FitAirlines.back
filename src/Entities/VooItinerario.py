from Entities.BaseModel import *
from Entities.Voo import *
from Entities.Itinerario import *

class VooItinerario(BaseModel):
    id_voo_itinerario = AutoField(column_name='ID_VOO_ITINERARIO')

    id_voo = ForeignKeyField(column_name='ID_VOO', field='id_voo', model=Voo)
    id_itinerario = ForeignKeyField(column_name='ID_ITINERARIO', field='id_itinerario', model=Itinerario)

    class Meta:
        table_name = 'voo_itinerario'