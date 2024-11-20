
def mostrar_barra_de_progresso(numero, tamanho_lista, info = ''):
    # Calcula a porcentagem de progresso
    progresso = (numero / tamanho_lista) * 100
    
    # Cria a barra de progresso com base na porcentagem
    barra = '#' * int(progresso // 2)  # A barra cresce com o progresso
    barra_restante = ' ' * (50 - len(barra))  # Preenche o restante da barra
    
    # Exibe a barra com a porcentagem, sobrescrevendo a linha anterior
    print(f"\r[{barra}{barra_restante}] {progresso:.2f}% {info}", end="", flush=True)

    if(progresso == 100):
        print('')
