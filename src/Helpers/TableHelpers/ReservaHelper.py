from Entities.Aeronave import Aeronave
from Entities.Assento import Assento
from Entities.Passageiro import Passageiro
from Entities.ReservaDeAssentoVoo import ReservaDeAssentoVoo
from Entities.BaseModel import database as db

import random
import datetime
import multiprocessing

def carregar_dados():
    """
    Carrega os dados necessários de aeronaves, assentos e passageiros de forma eficiente.
    """
    aeronaves = list(Aeronave.select())
    assentos = list(Assento.select())
    passageiros = list(Passageiro.select())
    return aeronaves, assentos, passageiros

def gerar_reservas_para_voos(voos_lote, aeronaves, assentos, passageiros):
    """
    Gera as reservas para um lote de voos, associando-os com os passageiros e assentos.
    """
    reservas = []
    for voo in voos_lote:
        # Encontrar a aeronave pelo ID
        aeronave = next((aeronave for aeronave in aeronaves if aeronave.id_aeronave == voo.ID_AERONAVE), None)
        if not aeronave:
            continue

        # Filtrar os assentos disponíveis para a aeronave
        assentos_aeronave = [assento for assento in assentos if assento.ID_AERONAVE == aeronave.id_aeronave]
        capacidade = aeronave.id_tipo_aeronave.capacidade_passageiros
        assentos_reservados = assentos_aeronave[:capacidade - voo.assentos_disponiveis]

        passageiros_no_voo = set()
        for assento in assentos_reservados:
            # Escolher um passageiro aleatório
            passageiro = random.choice([p for p in passageiros if p.id_passageiro not in passageiros_no_voo])
            passageiros_no_voo.add(passageiro.id_passageiro)

            reservas.append(ReservaDeAssentoVoo(
                id_passageiro=passageiro.id_passageiro,
                id_voo=voo.id_voo,
                id_assento=assento.id_assento,
                valor_total=voo.preco_base + assento.id_classe.preco_adicional,
                data=datetime.date.today()
            ))

    return reservas

def gerar_reservas_em_paralelo(voos, tamanho_lote=100, num_processos=4):
    """
    Gera as reservas de forma paralela utilizando multiprocessing.
    """
    print("Gerando Reservas...")
    aeronaves, assentos, passageiros = carregar_dados()
    total_voos = len(voos)
    reservas = []

    # Dividir voos em lotes
    lotes = [voos[i:i + tamanho_lote] for i in range(0, total_voos, tamanho_lote)]

    # Processamento paralelo
    with multiprocessing.Pool(processes=num_processos) as pool:
        # Usando starmap para passar os parâmetros de forma mais clara
        resultados = pool.starmap(
            gerar_reservas_para_voos,
            [(lote, aeronaves, assentos, passageiros) for lote in lotes]
        )

    # Achatar a lista de resultados de todos os subprocessos
    for reserva_lote in resultados:
        reservas.extend(reserva_lote)

    print("Reservas geradas com sucesso!")

    return reservas
