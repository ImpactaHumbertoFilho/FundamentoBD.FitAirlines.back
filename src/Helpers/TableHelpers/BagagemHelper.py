import random
import multiprocessing
from Entities.ReservaDeAssentoVoo import ReservaDeAssentoVoo

from Entities.ReservaBagagem import ReservaBagagem

def gerar_bagagens_para_reservas(reservas_lote):
    """
    Gera bagagens para um lote de reservas e retorna uma lista de objetos ReservaBagagem.
    
    Parâmetros:
    - reservas_lote: Lista de reservas com informações mínimas.

    Retorna:
    - Lista de objetos ReservaBagagem.
    """
    bagagens_geradas = []
    
    for reserva in reservas_lote:
        num_bagagens = 1 if random.randint(1, 15) != 1 else 2
        for i in range(num_bagagens):
            id_bagagem = random.randint(1, 2)  # Substitua por IDs reais de bagagens
            bagagens_geradas.append(ReservaBagagem(
                id_reserva_de_assento_voo=reserva.id_reserva_de_assento_voo,
                id_bagagem=id_bagagem,
            ))
    return bagagens_geradas

def gerar_bagagens_em_paralelo(num_processos=4, tamanho_lote=100):
    """
    Gera bagagens de forma paralela para reservas obtidas do banco de dados.
    
    Parâmetros:
    - num_processos: Número de processos paralelos.
    - tamanho_lote: Número de reservas por lote.
    
    Retorna:
    - Lista de dicionários representando todas as bagagens geradas.
    """
    print('Gerando Bagagens para reservas...')
    # Passo 1: Buscar reservas diretamente do banco
    reservas = list(ReservaDeAssentoVoo.select())
    
    # Passo 2: Dividir reservas em lotes
    lotes = [reservas[i:i + tamanho_lote] for i in range(0, len(reservas), tamanho_lote)]

    # Passo 3: Criar pool de processos
    with multiprocessing.Pool(processes=num_processos) as pool:
        resultados = pool.map(gerar_bagagens_para_reservas, lotes)
    
    # Passo 4: Concatenar resultados de todos os processos
    bagagens = [bagagem for resultado in resultados for bagagem in resultado]
    print('Bagagens geradas com sucesso!')
    return bagagens
