from faker import Faker

from Entities.BaseModel import database
from Entities.Passageiro import *
from Entities.Itinerario import *
from Entities.Voo import *
from Entities.VooItinerario import *
from Entities.Classe import *

from Helpers.FileHelper import execute_sql_file

from Helpers.TableHelpers.VooHelper import *
from Helpers.TableHelpers.ItinerarioHelper import *
from Helpers.TableHelpers.AssentoHelper import *

fake = Faker(['it_IT', 'pt_BR'])
fake.seed_instance(123)

# Criando o banco
execute_sql_file(database, 'SQL\\FIT-SCRIPT-GERAR.sql')

# Populando a tabela de aeroportos
execute_sql_file(database, 'SQL\\Data\\Aeroportos.sql')

# Populando a tabela de tipos de aeronaves
execute_sql_file(database, 'SQL\\Data\\TipoAeronave.sql')

# Populando a tabela de tipos de classes
execute_sql_file(database, 'SQL\\Data\\Classes.sql')

aeroportos = Aeroporto.select()

#gerando itinerarios
itinerarios = gerar_itinerarios_realistas(aeroportos, 200)

with database.atomic():
    Itinerario.bulk_create(itinerarios)

print(f'{len(itinerarios)} itinerarios incluidos...')

#gerando Voos e seus itinerarios
tipo_aeronaves = TipoAeronave.select()
voos, voos_itinerarios = gerar_voos_com_itinerarios(aeroportos, itinerarios, tipo_aeronaves, datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))

with database.atomic():
    Voo.bulk_create(voos)

print(f'{len(voos)} voos incluidos...')
    
with database.atomic():
    VooItinerario.bulk_create(voos_itinerarios)
    
print(f'{len(voos_itinerarios)} voos_itinerarios incluidos...')

#gerar assentos
classes = Classe.select()
assentos = gerar_assentos(voos, tipo_aeronaves, classes)

BATCH_SIZE = 10000  # Ajuste o tamanho do lote conforme necessário
with database.atomic():
    for i in range(0, len(assentos), BATCH_SIZE):
        Assento.bulk_create(assentos[i:i + BATCH_SIZE])

print(f'{len(assentos)} assentos incluidos...')

print(f'Incluindo passageiros...')
with database.atomic():
    for i in range(50000):
        Passageiro.create( 
            cpf=fake.cpf(), 
            email = fake.email(), 
            endereco=fake.address(), 
            nacionalidade = fake.country(), 
            nome = fake.name(), 
            telefone = fake.cellphone_number())

passageiros = Passageiro.select()

print(f'{len(passageiros)} Passageiros incluidos...')
