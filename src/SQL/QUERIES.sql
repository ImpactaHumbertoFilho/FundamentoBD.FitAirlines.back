select * from aeroporto a 

select * from tipo_aeronave ta 

select * from voo v

select * from relatorio r

select * from itinerario i 

select * from voo_itinerario vi

SELECT * from classe c 

SELECT * from assento a 

SELECT * from passageiro p 

SELECT * from reserva r 

select * from tipo_pagamento tp

select * from pagamento p

select * from ticket t


select 
	v.CODIGO,
	v.PARTIDA,
	v.CHEGADA,
	ta.CAPACIDADE_PASSAGEIROS,
	v.ASSENTOS_DISPONIVEIS,
	v.STATUS,
	ta.NOME,
	i.PARADAS,
	i.DISTANCIA_KM,
	i.DESCRICAO 
from 
	voo v
left join tipo_aeronave ta 
	on v.ID_TIPO_AERONAVE = ta.ID_TIPO_AERONAVE 
left join voo_itinerario vi 
	on vi.ID_VOO = v.ID_VOO
left join itinerario i  
	on vi.ID_ITINERARIO = i.ID_ITINERARIO
where
	v.STATUS != "finalizado"

SELECT count(*) from assento a

select
	sum(ta.CAPACIDADE_PASSAGEIROS)
from 
	voo v
left join tipo_aeronave ta 
	on v.ID_TIPO_AERONAVE = ta.ID_TIPO_AERONAVE 
left join voo_itinerario vi 
	on vi.ID_VOO = v.ID_VOO
left join itinerario i  
	on vi.ID_ITINERARIO = i.ID_ITINERARIO


