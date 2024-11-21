import random
from datetime import datetime, timedelta
from multiprocessing import Pool

from Entities.Pagamento import Pagamento

def gerar_pagamento_para_reserva(reserva, tipos_pagamento, taxa_falha=1000):
    """
    Gera pagamentos para uma única reserva, com uma chance de falha definida.

    Parâmetros:
    - reserva: Objeto de ReservaDeAssentoVoo.
    - tipos_pagamento: Lista de objetos de TipoPagamento.
    - taxa_falha: Probabilidade de falha (1 em taxa_falha).

    Retorna:
    - Lista de objetos de Pagamento gerados para a reserva.
    """
    pagamentos = []

    # Escolher tipo de pagamento aleatório
    tipo_pagamento = random.choice(tipos_pagamento)

    # Decidir se o pagamento inicial falha
    pagamento_falhado = random.randint(1, taxa_falha) == 1

    pagamento = Pagamento(
        id_reserva_de_assento_voo=reserva.id_reserva_de_assento_voo,
        id_tipo_pagamento=tipo_pagamento.id_tipo_pagamento,
        valor_total=reserva.valor_total,
        status="APROVADO",
        data_pagamento=datetime.now()
    )

    if pagamento_falhado:
        pagamento.status = 'CANCELADO'

        # Pagamento bem-sucedido após o falhado
        pagamentos.append(Pagamento(
            id_reserva_de_assento_voo=reserva.id_reserva_de_assento_voo,
            id_tipo_pagamento=tipo_pagamento.id_tipo_pagamento,
            valor_total=reserva.valor_total,
            status="APROVADO",
            data_pagamento=datetime.now() + timedelta(minutes=2)  # Simular tempo depois do falhado
        ))

    pagamentos.append(pagamento)
    
    return pagamentos


def gerar_pagamentos_em_lote(reservas, tipos_pagamento, taxa_falha=1000, num_processos=4):
    """
    Gera pagamentos para uma lista de reservas de forma paralela usando multiprocessing.

    Parâmetros:
    - reservas: Lista de objetos de ReservaDeAssentoVoo.
    - tipos_pagamento: Lista de objetos de TipoPagamento.
    - taxa_falha: Probabilidade de falha (1 em taxa_falha).
    - num_processos: Número de processos a serem usados. Se None, usa o número de CPUs disponíveis.

    Retorna:
    - Lista de objetos de Pagamento representando todos os pagamentos gerados.
    """
    print('Gerando pagamentos...')

    # Criar o pool de processos
    with Pool(processes=num_processos) as pool:
        # Mapeia cada reserva para o processo de geração de pagamento
        resultados = pool.starmap(
            gerar_pagamento_para_reserva,
            [(reserva, tipos_pagamento, taxa_falha) for reserva in reservas]
        )

    # Achatar a lista de listas em uma única lista de pagamentos
    pagamentos = [pagamento for sublist in resultados for pagamento in sublist]
    
    print('Pagamentos gerados com sucesso!')
    return pagamentos