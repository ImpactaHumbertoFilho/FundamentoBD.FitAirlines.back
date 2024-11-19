from Entities.VooItinerario import VooItinerario
from Entities.Voo import Voo

import random
import datetime

def gerar_voos_com_itinerarios(aeroportos, itinerarios, tipos_aeronave, inicio, fim):
    voos = []
    voo_itinerarios = []
    status_opcoes = ["programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado","programado", "cancelado"]

    delta = datetime.timedelta(days=1)
    codigo_voo = 1000

    i = 1
    while inicio <= fim:

        comeco_itinerarios = random.randint(0, len(itinerarios))
        fim_itinerarios = random.randint(comeco_itinerarios, len(itinerarios))

        itinerarios_do_delta = itinerarios[comeco_itinerarios:fim_itinerarios]
        for itinerario in itinerarios_do_delta:
            
            origem = [aero for aero in aeroportos if aero.codigo == itinerario.paradas[0]][0]
            destino = [aero for aero in aeroportos if aero.codigo == itinerario.paradas[-1]][0]

            if origem.id_aeroporto != destino.id_aeroporto:
                # Escolher aleatoriamente uma aeronave da lista de tipos
                tipo_aeronave = random.choice(tipos_aeronave)
                
                partida_hora = datetime.datetime.combine(
                    inicio, datetime.time(random.randint(0, 23), random.randint(0, 59))
                )
                duracao_horas = itinerario.duracao  # A duração vem do itinerário
                chegada_hora = partida_hora + datetime.timedelta(hours=duracao_horas)
                
                if(chegada_hora.date() < datetime.date.today()):
                    status = "finalizado"
                elif(chegada_hora.date() == datetime.date.today()):
                    status = "em andamento"
                else:
                    status = random.choice(status_opcoes)
                
                assentos_disponiveis = random.randint(0, tipo_aeronave.capacidade_passageiros)

                # Criar objeto Voo
                voo = Voo(
                    id_voo = i,
                    id_tipo_aeronave=tipo_aeronave.id_tipo_aeronave,  # Usando o ID da aeronave
                    id_aeroporto_partida=origem.id_aeroporto,
                    id_aeroporto_chegada=destino.id_aeroporto,
                    
                    codigo=f"V-{codigo_voo}",
                    partida=partida_hora,
                    chegada=chegada_hora,
                    duracao=round(duracao_horas, 2),
                    assentos_disponiveis=assentos_disponiveis,
                    status=status
                )

                # Criar objeto VooItinerario
                voo_itinerario = VooItinerario(id_voo=i, id_itinerario=itinerarios.index(itinerario) + 1)

                # Adicionar à lista de voos e voo_itinerarios
                voos.append(voo)
                voo_itinerarios.append(voo_itinerario)

                codigo_voo += 1
                i +=1

        inicio += delta

    return voos, voo_itinerarios
