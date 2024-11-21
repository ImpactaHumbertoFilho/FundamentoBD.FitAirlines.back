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
from Entities.Bagagem import *
from Entities.TipoPagamento import *
from Entities.ReservaBagagem import *
from Entities.Pagamento import *
from Entities.Relatorio import *

from Helpers.FileHelper import execute_sql_file

from Helpers.TableHelpers.VooHelper import *
from Helpers.TableHelpers.ItinerarioHelper import *
from Helpers.TableHelpers.AssentoHelper import *
from Helpers.TableHelpers.ReservaHelper import gerar_reservas_em_paralelo
from Helpers.TableHelpers.PassageirosHelper import *
from Helpers.TableHelpers.BagagemHelper import gerar_bagagens_em_paralelo
from Helpers.TableHelpers.PagamentoHelper import gerar_pagamentos_em_lote
from Helpers.TableHelpers.RelatorioHelper import gerar_relatorios_para_voos

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

    def carga_TiposPagamento():
        execute_sql_file(database, 'SQL\\Data\\TiposPagamento.sql')

    #gerando itinerarios
    def carga_ininerarios(aeroportos):
        itinerarios = gerar_itinerarios_realistas(aeroportos, 200)

        with database.atomic():
            Itinerario.bulk_create(itinerarios)

        return itinerarios

    #gerando Voos e seus itinerarios
    def carga_voos_e_itinerarios_de_voos(aeroportos, itinerarios, aeronaves):
        voos, voos_itinerarios = gerar_voos_com_itinerarios(aeroportos, itinerarios, aeronaves, date(2024, 1, 1), date(2024, 12, 31))

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

    #gerar bagagens
    def carga_bagagens_para_reservas():
        bagagens_reservas = gerar_bagagens_em_paralelo()

        with database.atomic():
            for i in range(0, len(bagagens_reservas), BATCH_SIZE):
                ReservaBagagem.bulk_create(bagagens_reservas[i:i + BATCH_SIZE])

    def carga_pagamentos(reservas, tipos_pagamento):
        reservas = list(reservas)
        tipos_pagamento = list(tipos_pagamento)

        pagamentos = gerar_pagamentos_em_lote(reservas, tipos_pagamento)
        
        with database.atomic():
            for i in range(0, len(pagamentos), BATCH_SIZE):
                Pagamento.bulk_create(pagamentos[i:i + BATCH_SIZE])
    
    def carga_reservas(voos):
        reservas = gerar_reservas_em_paralelo(voos)
        
        with database.atomic():
            for i in range(0, len(reservas), BATCH_SIZE):
                ReservaDeAssentoVoo.bulk_create(reservas[i:i + BATCH_SIZE])

    def carga_relatorios():
        relatorios = gerar_relatorios_para_voos()
        
        with database.atomic():
            for i in range(0, len(relatorios), BATCH_SIZE):
                Relatorio.bulk_create(relatorios[i:i + BATCH_SIZE])


    def carga_completa():
        criar_banco()

        # dados padrao
        carga_aeroportos()
        carga_bagagens()
        carga_tipo_aeronaves()
        carga_aeronaves()
        carga_classes()
        carga_TiposPagamento()
        
        aeroportos = Aeroporto.select()
        aeronaves = Aeronave.select()
        classes = Classe.select()
        tipos_aeronave = TipoAeronave.select()
        tipos_pagamento = TipoPagamento.select()

        # Carga personalizada
        itinerarios = carga_ininerarios(aeroportos)
        carga_voos_e_itinerarios_de_voos(aeroportos, itinerarios, aeronaves)
        
        carga_assentos(aeronaves, classes, tipos_aeronave)
        carga_passageiros()
        
        voos = Voo.select()
        carga_relatorios()

        reservas = carga_reservas(voos)

        carga_bagagens_para_reservas()

        reservas = ReservaDeAssentoVoo.select()
        carga_pagamentos(reservas, tipos_pagamento)

        #fazer o ticket
        #fazer o relatorio


    # Criando o banco
    carga_completa()
