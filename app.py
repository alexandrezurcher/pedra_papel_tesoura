import random
name = input('digite o nome do jogador: ')

while True:
    input_jogador = input(f'{name} - Escolha uma - pedra|papel|tesoura: ')
    lista = ['pedra','papel','tesoura']
    input_computador = random.choice(lista)
    if input_jogador == 'pedra':
        if input_computador == 'pedra':
            print(f'EMPATOU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.')
        if input_computador == 'papel':
            print(f'PERDEU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.') 
        if input_computador == 'tesoura':
            print(f'GANHOU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.')
    elif input_jogador == 'papel':
        if input_computador == 'papel':
            print(f'EMPATOU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.')
        if input_computador == 'tesoura':
            print(f'PERDEU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.') 
        if input_computador == 'pedra':
            print(f'GANHOU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.')                 
    elif input_jogador == 'tesoura':
        if input_computador == 'tesoura':
            print(f'EMPATOU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.')
        if input_computador == 'pedra':
            print(f'PERDEU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.') 
        if input_computador == 'papel':
            print(f'GANHOU - bot escolheu: {input_computador}, {name} escolheu {input_jogador}.')
    else:
        print('resposta invalida, reiniciando o jogo')         



