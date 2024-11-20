from Entities.Passageiro import Passageiro
from Helpers.porcentagemHelper import mostrar_barra_de_progresso

from faker import Faker

def gerar_passageiros(qntd_passageiros):
    fake = Faker(['it_IT', 'pt_BR'])
    fake.seed_instance(123)

    passageiros = []
    for i in range(qntd_passageiros):
        passageiro = Passageiro( 
            cpf=fake.cpf(), 
            email = fake.email(), 
            endereco=fake.address(), 
            nacionalidade = fake.country(), 
            nome = fake.name(), 
            telefone = fake.cellphone_number(),
            data_nascimento = fake.date_of_birth()
        )
        
        passageiros.append(passageiro)
        mostrar_barra_de_progresso(i + 1, qntd_passageiros, 'carga de passageiros.')

    return passageiros
