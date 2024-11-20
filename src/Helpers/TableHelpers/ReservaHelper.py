from Entities.Aeronave import Aeronave
from Entities.Assento import Assento
from Entities.Passageiro import Passageiro
from Entities.ReservaDeAssentoVoo import ReservaDeAssentoVoo
from Helpers.porcentagemHelper import mostrar_barra_de_progresso

from Entities.BaseModel import database as db

import random
import datetime
import multiprocessing

def carregar_dados():
    aeronaves = {aeronave.id_aeronave: aeronave for aeronave in Aeronave.select()}
    assentos_por_aeronave = {
        id_aeronave: list(Assento.select().where(Assento.id_aeronave == id_aeronave))
        for id_aeronave in aeronaves
    }
    passageiros = list(Passageiro.select())  # Carregar todos os passageiros na memória
    return aeronaves, assentos_por_aeronave, passageiros

def salvar_reservas_em_lote(reservas, tamanho_lote=10000):
    with db.atomic():  # Usando transações em massa
        for inicio in range(0, len(reservas), tamanho_lote):
            lote = reservas[inicio:inicio + tamanho_lote]
            
            # Verificar se o lote não está vazio
            if not lote:
                continue

            # Converter objetos em dicionários para a inserção
            dados_para_inserir = [
                {
                    "id_passageiro": r.id_passageiro,
                    "id_voo": r.id_voo,
                    "id_assento": r.id_assento,
                    "valor_total": r.valor_total,
                    "data": r.data
                }
                for r in lote
            ]

            # Inserção em bulk
            ReservaDeAssentoVoo.insert_many(dados_para_inserir).execute()

def gerar_reservas_para_voos(voos_lote, aeronaves, assentos_por_aeronave, passageiros, progresso_lista, indice_thread, total_voos):
    reservas = []
    for i, voo in enumerate(voos_lote, start=1):
        aeronave = aeronaves.get(voo.ID_AERONAVE)
        if not aeronave:
            continue

        assentos = assentos_por_aeronave.get(aeronave.id_aeronave, [])
        capacidade = aeronave.id_tipo_aeronave.capacidade_passageiros
        assentos_reservados = assentos[:capacidade - voo.assentos_disponiveis]

        passageiros_no_voo = set()
        for assento in assentos_reservados:
            passageiro = random.choice([p for p in passageiros if p.id_passageiro not in passageiros_no_voo])
            passageiros_no_voo.add(passageiro.id_passageiro)

            reservas.append(ReservaDeAssentoVoo(
                id_passageiro=passageiro.id_passageiro,
                id_voo=voo.id_voo,
                id_assento=assento.id_assento,
                valor_total=voo.preco_base + assento.id_classe.preco_adicional,
                data=datetime.date.today()
            ))

        # Atualizando progresso na lista compartilhada
        progresso = (i / total_voos) * 100
        progresso_lista[indice_thread] = progresso  # Atualiza o progresso na lista

    return reservas
def gerar_reservas_em_paralelo(voos, tamanho_lote=100, num_processos=4):
    aeronaves, assentos_por_aeronave, passageiros = carregar_dados()
    total_voos = len(voos)
    reservas = []

    # Dividir voos em lotes
    lotes = [voos[i:i + tamanho_lote] for i in range(0, total_voos, tamanho_lote)]

    # Configuração do progresso (usando Manager para compartilhamento)
    with multiprocessing.Manager() as manager:
        progresso_lista = manager.list([0] * len(lotes))  # Alinha o progresso com o número de lotes
        total_lotes = len(lotes)

        # Processamento paralelo
        with multiprocessing.Pool(processes=num_processos) as pool:
            resultados = []
            for indice_thread, lote in enumerate(lotes):
                resultados.append(pool.apply_async(
                    gerar_reservas_para_voos, 
                    (lote, aeronaves, assentos_por_aeronave, passageiros, progresso_lista, indice_thread, total_voos)
                ))

            # Processamento do progresso enquanto os lotes são processados
            while len(resultados) > 0:
                for r in resultados:
                    if r.ready():
                        reservas.extend(r.get())  # Concatena os resultados de cada subprocesso
                        resultados.remove(r)

                # Exibir progresso atualizado
                for i, progresso in enumerate(progresso_lista):
                    mostrar_barra_de_progresso(i, total_lotes, f"Progresso {i+1}: {progresso:.2f}%")

    # Salvar todas as reservas em lote
    salvar_reservas_em_lote(reservas)
    print("\nReservas geradas e salvas com sucesso!")
