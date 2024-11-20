from peewee import *

database = MySQLDatabase('fitairlines', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'user': 'root', 'password': '3025'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class TipoAeronave(BaseModel):
    capacidade_passageiros = IntegerField(column_name='CAPACIDADE_PASSAGEIROS', null=True)
    descricao = CharField(column_name='DESCRICAO', null=True)
    fabricante = CharField(column_name='FABRICANTE', null=True)
    id_tipo_aeronave = AutoField(column_name='ID_TIPO_AERONAVE')
    nome = CharField(column_name='NOME', null=True)

    class Meta:
        table_name = 'tipo_aeronave'

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

class Aeroporto(BaseModel):
    capacidade = IntegerField(column_name='CAPACIDADE', null=True)
    cidade = CharField(column_name='CIDADE', null=True)
    codigo = CharField(column_name='CODIGO', null=True)
    estado = CharField(column_name='ESTADO', null=True)
    id_aeroporto = AutoField(column_name='ID_AEROPORTO')
    latitude = DecimalField(column_name='LATITUDE', null=True)
    longitude = DecimalField(column_name='LONGITUDE', null=True)
    nome = CharField(column_name='NOME', null=True)
    pais = CharField(column_name='PAIS', null=True)

    class Meta:
        table_name = 'aeroporto'

class Classe(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    id_classe = AutoField(column_name='ID_CLASSE')
    nome = CharField(column_name='NOME', null=True)
    preco_adicional = DecimalField(column_name='PRECO_ADICIONAL', null=True)
    prioridade = IntegerField(column_name='PRIORIDADE', null=True)
    tipo = CharField(column_name='TIPO', null=True)

    class Meta:
        table_name = 'classe'

class Assento(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    id_aeronave = ForeignKeyField(column_name='ID_AERONAVE', field='id_aeronave', model=Aeronave)
    id_assento = IntegerField(column_name='ID_ASSENTO', unique=True)
    id_classe = ForeignKeyField(column_name='ID_CLASSE', field='id_classe', model=Classe)
    localizacao = CharField(column_name='LOCALIZACAO', null=True)
    numero = CharField(column_name='NUMERO', null=True)

    class Meta:
        table_name = 'assento'
        indexes = (
            (('id_assento', 'id_classe', 'id_aeronave'), True),
        )
        primary_key = CompositeKey('id_aeronave', 'id_assento', 'id_classe')

class Bagagem(BaseModel):
    dimensoes = CharField(column_name='DIMENSOES', null=True)
    id_bagagem = AutoField(column_name='ID_BAGAGEM')
    peso_kg = DecimalField(column_name='PESO_KG', null=True)
    preco_adicional = DecimalField(column_name='PRECO_ADICIONAL', null=True)
    tipo_bagagem = CharField(column_name='TIPO_BAGAGEM')

    class Meta:
        table_name = 'bagagem'

class Itinerario(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    distancia_km = FloatField(column_name='DISTANCIA_KM', null=True)
    duracao = TimeField(column_name='DURACAO', null=True)
    id_itinerario = AutoField(column_name='ID_ITINERARIO')
    paradas = CharField(column_name='PARADAS', null=True)

    class Meta:
        table_name = 'itinerario'

class Voo(BaseModel):
    assentos_disponiveis = IntegerField(column_name='ASSENTOS_DISPONIVEIS', null=True)
    chegada = DateTimeField(column_name='CHEGADA', null=True)
    codigo = CharField(column_name='CODIGO', null=True)
    duracao = TimeField(column_name='DURACAO', null=True)
    id_aeronave = ForeignKeyField(column_name='ID_AERONAVE', field='id_aeronave', model=Aeronave)
    id_aeroporto_chegada = ForeignKeyField(column_name='ID_AEROPORTO_CHEGADA', field='id_aeroporto', model=Aeroporto)
    id_aeroporto_partida = ForeignKeyField(backref='aeroporto_id_aeroporto_partida_set', column_name='ID_AEROPORTO_PARTIDA', field='id_aeroporto', model=Aeroporto)
    id_voo = IntegerField(column_name='ID_VOO')
    partida = DateTimeField(column_name='PARTIDA', null=True)
    preco_base = DecimalField(column_name='PRECO_BASE', null=True)
    status = CharField(column_name='STATUS', null=True)

    class Meta:
        table_name = 'voo'
        indexes = (
            (('id_voo', 'id_aeronave', 'id_aeroporto_partida', 'id_aeroporto_chegada'), True),
        )
        primary_key = CompositeKey('id_aeronave', 'id_aeroporto_chegada', 'id_aeroporto_partida', 'id_voo')

class Passageiro(BaseModel):
    cpf = CharField(column_name='CPF', null=True)
    data_nascimento = DateTimeField(column_name='DATA_NASCIMENTO', null=True)
    email = CharField(column_name='EMAIL', null=True)
    endereco = CharField(column_name='ENDERECO', null=True)
    id_passageiro = AutoField(column_name='ID_PASSAGEIRO')
    nacionalidade = CharField(column_name='NACIONALIDADE', null=True)
    nome = CharField(column_name='NOME', null=True)
    telefone = CharField(column_name='TELEFONE', null=True)

    class Meta:
        table_name = 'passageiro'

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

class TipoPagamento(BaseModel):
    descricao = CharField(column_name='DESCRICAO', null=True)
    id_tipo_pagamento = AutoField(column_name='ID_TIPO_PAGAMENTO')
    tipo = CharField(column_name='TIPO', null=True)

    class Meta:
        table_name = 'tipo_pagamento'

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

class Relatorio(BaseModel):
    clima = CharField(column_name='CLIMA', null=True)
    data = DateTimeField(column_name='DATA', null=True)
    descricao = CharField(column_name='DESCRICAO', null=True)
    desembarque = DateTimeField(column_name='DESEMBARQUE', null=True)
    embarque = DateTimeField(column_name='EMBARQUE', null=True)
    id_relatorio = IntegerField(column_name='ID_RELATORIO')
    id_voo = ForeignKeyField(column_name='ID_VOO', field='id_voo', model=Voo)
    tempo = CharField(column_name='TEMPO', null=True)

    class Meta:
        table_name = 'relatorio'
        indexes = (
            (('id_relatorio', 'id_voo'), True),
        )
        primary_key = CompositeKey('id_relatorio', 'id_voo')

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

