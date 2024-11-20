select * from aeroporto a 

select * from tipo_aeronave ta 

select * from voo v

select * from relatorio r

select * from itinerario i 

select * from voo_itinerario vi

SELECT * from classe c 

SELECT * from assento a 

SELECT * from passageiro p 

select count(*) from reserva_de_assento_voo rdav 

select * from tipo_pagamento tp

select * from pagamento p

select * from ticket t

select * from reserva_bagagem rb

select * from bagagem b

select 
	v.CODIGO,
	v.PARTIDA,
	v.CHEGADA,
	ta.CAPACIDADE_PASSAGEIROS,
	v.ASSENTOS_DISPONIVEIS,
	v.STATUS,
	a.CODIGO,
	ta.NOME,
	i.PARADAS,
	i.DISTANCIA_KM,
	i.DESCRICAO 
from 
	voo v
left join aeronave a 
	on v.ID_AERONAVE = a.ID_AERONAVE 
left join tipo_aeronave ta 
	on a.ID_TIPO_AERONAVE = ta.ID_TIPO_AERONAVE 
left join voo_itinerario vi 
	on vi.ID_VOO = v.ID_VOO
left join itinerario i  
	on vi.ID_ITINERARIO = i.ID_ITINERARIO
where
	v.STATUS != "finalizado"

SELECT count(*) from assento a

select
	*
from 
	voo v
left join aeronave a 
	on v.ID_AERONAVE = a.ID_AERONAVE 
left join tipo_aeronave ta 
	on a.ID_TIPO_AERONAVE = ta.ID_TIPO_AERONAVE
left join assento a2
	on a2.ID_AERONAVE = a.ID_AERONAVE 


