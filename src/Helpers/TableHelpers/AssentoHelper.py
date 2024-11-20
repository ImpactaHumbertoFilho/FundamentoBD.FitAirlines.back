from Entities.Assento import Assento
from Helpers.porcentagemHelper import mostrar_barra_de_progresso

import random

def gerar_assentos(aeronaves, tipos_aeronave, classes):
    """
    Gera uma lista de assentos para cada aeronave.

    :param aeronaves: Lista de objetos da classe Aeronave.
    :param tipos_aeronave: Lista de objetos da classe TipoAeronave.
    :param classes: Lista de objetos da classe Classe.
    :return: Lista de objetos Assento.
    """
    
    assentos = []

    i = 0
    for aeronave in aeronaves:
        # Encontrar o tipo de aeronave correspondente ao aeronave
        tipo_aeronave = next(
            (ta for ta in tipos_aeronave if aeronave.ID_TIPO_AERONAVE == ta.id_tipo_aeronave), None
        )

        if not tipo_aeronave:
            continue  # Se não encontrar o tipo de aeronave, pula o aeronave

        capacidade = tipo_aeronave.capacidade_passageiros

        # Escolher uma classe aleatória para os assentos
        classe = random.choice(classes)

        for numero in range(1, capacidade + 1):
            assento = Assento(
                descricao= f"Assento {numero}",
                id_classe= classe.id_classe,
                id_aeronave= aeronave.id_aeronave,
                localizacao= f"{'A' if numero % 2 == 0 else 'B'}{(numero - 1) // 6 + 1}",
                numero= f"{numero:03}",
            )
            assentos.append(assento)

        i +=1
        mostrar_barra_de_progresso(i, len(aeronaves), 'carga de assentos.')
        
    return assentos