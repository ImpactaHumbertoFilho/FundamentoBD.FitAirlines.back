from Entities.BaseModel import *
from Entities.TipoAeronave import TipoAeronave

class Aeronave(BaseModel):
    ano_fabricacao = UnknownField(column_name='ANO_FABRICACAO', null=True)  # year
    codigo = CharField(column_name='CODIGO', null=True)
    horas_voadas = DecimalField(column_name='HORAS_VOADAS', constraints=[SQL("DEFAULT 0.00")], null=True)
    id_aeronave = IntegerField(column_name='ID_AERONAVE')
    id_tipo_aeronave = ForeignKeyField(column_name='ID_TIPO_AERONAVE', field='id_tipo_aeronave', model=TipoAeronave)
    modelo = CharField(column_name='MODELO', null=True)
    status = CharField(column_name='STATUS', constraints=[SQL("DEFAULT 'ATIVA'")], null=True)

    class Meta:
        table_name = 'aeronave'
        indexes = (
            (('id_aeronave', 'id_tipo_aeronave'), True),
        )
        primary_key = CompositeKey('id_aeronave', 'id_tipo_aeronave')
