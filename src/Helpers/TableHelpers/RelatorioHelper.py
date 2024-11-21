from Entities.Relatorio import Relatorio
from Entities.Voo import Voo

from Helpers.porcentagemHelper import mostrar_barra_de_progresso

import datetime
from datetime import date
import random

def gerar_relatorios_para_voos():
        voos_finalizados = list(Voo.select().where(Voo.status == "FINALIZADO"))
        relatorios_gerados = []  # Lista para armazenar os relatórios gerados

        i = 0
        for voo in voos_finalizados:

            clima = random.choice(["Desconhecido", "Ensolarado", "Chuva"])

            # Criar o relatorio para cada voo
            relatorio = Relatorio.create(
                id_voo=voo.id_voo,
                clima= clima,  # Exemplo de valor, pode ser ajustado conforme necessário
                descricao="Descrição do voo",  # Exemplo de valor, pode ser ajustado conforme necessário
                desembarque=voo.chegada,  # Supondo que o desembarque seja a data de chegada do voo
                embarque=voo.partida,  # Supondo que o embarque seja a data de partida do voo
                tempo= (voo.chegada - voo.partida),  # Exemplo de valor, pode ser ajustado conforme necessário
                data=datetime.date.today(),  # Data e hora da criação do relatório
            )
            relatorios_gerados.append(relatorio)  # Adiciona o relatório à lista
            
            i +=1
            mostrar_barra_de_progresso(i, len(voos_finalizados), 'carga de relatorios.')
        
        return relatorios_gerados