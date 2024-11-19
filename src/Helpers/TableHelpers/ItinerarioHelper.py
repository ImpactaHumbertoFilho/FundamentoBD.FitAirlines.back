import random
from math import radians, sin, cos, sqrt, atan2

from Entities.Itinerario import Itinerario

# Fórmula de Haversine para calcular distância em km
def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  # Raio médio da Terra em km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

# Gerar itinerários com paradas como lista de códigos
def gerar_itinerarios_realistas(aeroportos, qtd_itinerarios=20):
    itinerarios = []
    
    for _ in range(qtd_itinerarios):
        origem = random.choice(aeroportos)
        destino = random.choice(aeroportos)
        
        if origem.id_aeroporto != destino.id_aeroporto:
            distancia_km = calcular_distancia(
                origem.latitude, origem.longitude, destino.latitude, destino.longitude
            )
            
            paradas = [origem.codigo]
            if origem.pais != destino.pais:
                paradas = random.sample(
                    [aero.codigo for aero in aeroportos if aero.id_aeroporto not in [origem.id_aeroporto, destino.id_aeroporto]],
                    k=random.randint(0, min(3, len(aeroportos) - 2))
                )
            paradas.append(destino.codigo)
            
            duracao_horas = distancia_km / 900  # Velocidade média de 900 km/h
            
            descricao = f"De {origem.nome} para {destino.nome}"
            descricao += f' com paradas em {', '.join(paradas)}.' if len(paradas) > 0 else '.'

            itinerarios.append(Itinerario(descricao = descricao, distancia_km = round(distancia_km, 2), duracao = round(duracao_horas), paradas = paradas))
    
    return itinerarios