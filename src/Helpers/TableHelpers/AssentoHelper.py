from Entities.Assento import Assento

import random

def gerar_assentos(voos, tipos_aeronave, classes):
    """
    Gera uma lista de assentos para cada voo.

    :param voos: Lista de objetos da classe Voo.
    :param tipos_aeronave: Lista de objetos da classe TipoAeronave.
    :param classes: Lista de objetos da classe Classe.
    :return: Lista de objetos Assento.
    """
    
    print(f'gerando assentos...')
    assentos = []

    for voo in voos:
        # Encontrar o tipo de aeronave correspondente ao voo
        tipo_aeronave = next(
            (ta for ta in tipos_aeronave if voo.id_tipo_aeronave.id_tipo_aeronave == ta.id_tipo_aeronave), None
        )

        if not tipo_aeronave:
            continue  # Se não encontrar o tipo de aeronave, pula o voo

        capacidade = tipo_aeronave.capacidade_passageiros
        ocupados = capacidade - voo.assentos_disponiveis

        # Escolher uma classe aleatória para os assentos
        classe = random.choice(classes)

        for numero in range(1, capacidade + 1):
            assento = Assento(
                descricao= f"Assento {numero}",
                id_classe= classe.id_classe,
                id_voo= voo.id_voo,
                localizacao= f"{'A' if numero % 2 == 0 else 'B'}{(numero - 1) // 6 + 1}",
                numero= f"{numero:03}",
                ocupado= 1 if numero <= ocupados else 0,
            )
            assentos.append(assento)

    print(f'{len(assentos)} assentos gerados...')
    return assentos