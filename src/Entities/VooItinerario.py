from Entities.BaseModel import *
from Entities.Voo import *
from Entities.Itinerario import *

class VooItinerario(BaseModel):
    id_itinerario = ForeignKeyField(column_name='ID_ITINERARIO', field='id_itinerario', model=Itinerario)
    id_voo = ForeignKeyField(column_name='ID_VOO', field='id_voo', model=Voo)
    id_voo_itinerario = IntegerField(column_name='ID_VOO_ITINERARIO')

    class Meta:
        table_name = 'voo_itinerario'
        indexes = (
            (('id_voo_itinerario', 'id_voo', 'id_itinerario'), True),
        )
        primary_key = CompositeKey('id_itinerario', 'id_voo', 'id_voo_itinerario')

