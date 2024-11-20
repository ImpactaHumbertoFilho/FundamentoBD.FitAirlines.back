from faker import Faker

from datetime import date

from Entities.BaseModel import database
from Entities.Passageiro import *
from Entities.Itinerario import *
from Entities.Voo import *
from Entities.VooItinerario import *
from Entities.Classe import *
from Entities.Aeronave import *
from Entities.ReservaDeAssentoVoo import *

from Helpers.FileHelper import execute_sql_file

from Helpers.TableHelpers.VooHelper import *
from Helpers.TableHelpers.ItinerarioHelper import *
from Helpers.TableHelpers.AssentoHelper import *
from Helpers.TableHelpers.ReservaHelper import gerar_reservas_em_paralelo
from Helpers.TableHelpers.PassageirosHelper import *

BATCH_SIZE = 100000
if __name__ == "__main__":
    def criar_banco():
        execute_sql_file(database, 'SQL\\FIT-SCRIPT-GERAR.sql')

    def carga_aeroportos():
        execute_sql_file(database, 'SQL\\Data\\Aeroportos.sql')

    def carga_bagagens():
        execute_sql_file(database, 'SQL\\Data\\Bagagens.sql')

    def carga_tipo_aeronaves():
        execute_sql_file(database, 'SQL\\Data\\TipoAeronave.sql')

    def carga_aeronaves():
        execute_sql_file(database, 'SQL\\Data\\Aeronaves.sql')

    def carga_classes():
        execute_sql_file(database, 'SQL\\Data\\Classes.sql')

    #gerando itinerarios
    def carga_ininerarios(aeroportos):
        itinerarios = gerar_itinerarios_realistas(aeroportos, 200)

        with database.atomic():
            Itinerario.bulk_create(itinerarios)

        return itinerarios

    #gerando Voos e seus itinerarios
    def carga_voos_e_itinerarios_de_voos(aeroportos, itinerarios, aeronaves):
        voos, voos_itinerarios = gerar_voos_com_itinerarios(aeroportos, itinerarios, aeronaves, date(2024, 11, 1), date(2024, 12, 31))

        with database.atomic():
            Voo.bulk_create(voos)

        with database.atomic():
            VooItinerario.bulk_create(voos_itinerarios)

    #gerar assentos
    def carga_assentos(aeronaves, classes, tipos_aeronave):
        assentos = gerar_assentos(aeronaves, tipos_aeronave, classes)

        with database.atomic():
            for i in range(0, len(assentos), BATCH_SIZE):
                Assento.bulk_create(assentos[i:i + BATCH_SIZE])

        return assentos

    #gerar passageiros
    def carga_passageiros():
        passageiros = gerar_passageiros(5000)

        with database.atomic():
            Passageiro.bulk_create(passageiros)

        return passageiros

    #gerar reservas
    def carga_reservas(voos):
        reservas = gerar_reservas_para_voos(voos)

        with database.atomic():
            for i in range(0, len(reservas), BATCH_SIZE):
                ReservaDeAssentoVoo.bulk_create(reservas[i:i + BATCH_SIZE])

        return reservas

    def carga_completa():
        
        criar_banco()

        # dados padrao
        carga_aeroportos()
        carga_bagagens()
        carga_tipo_aeronaves()
        carga_aeronaves()
        carga_classes()
        
        aeroportos = Aeroporto.select()
        aeronaves = Aeronave.select()
        classes = Classe.select()
        tipos_aeronave = TipoAeronave.select()

        # Carga personalizada
        itinerarios = carga_ininerarios(aeroportos)
        carga_voos_e_itinerarios_de_voos(aeroportos, itinerarios, aeronaves)
        
        assentos = carga_assentos(aeronaves, classes, tipos_aeronave)
        passageiros = carga_passageiros()
        
        voos = Voo.select()
        reservas = gerar_reservas_em_paralelo(voos)


    # Criando o banco
    carga_completa()
