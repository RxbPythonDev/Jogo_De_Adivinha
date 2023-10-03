from random import randint

#Função para parar o jogo caso algum jogador digite "0"
def desistencia(*palpites):
    desistir = 0
    for palpite in palpites:
        if palpite == desistir:
            print('Desistencia do jogador, encerrando jogo.')
            print('FIM DE JOGO!')
            quit()

#Função para rodar o modo de jogo "1 Jogador"
def modo_solo():
    numero = randint(1, 100)
    tentativa = 1
    while True:
        palpite = input('Diga seu palpite: ')
        try:
            palpite = int(palpite)
        except ValueError:
            print('Palpite inválido, certifique-se de digitar um número inteiro. Exemplos: 1, 10, 100')
            continue
        desistencia(palpite)
        if palpite < 0 or palpite > 100:
            print('O número é gerado entre 1 e 100, caso deseje sair do jogo digite 0.')
            continue
        if palpite == numero:
            print(f'PARABÉNS!!! Você acertou em {tentativa} tentativa(s).')
            break
        elif palpite < numero:
            print(f'O número é maior que {palpite}!')
        else:
            print(f'O número é menor que {palpite}!')
        tentativa += 1
        
#Função para o modo "2 Jogadores 1 Número"     
def mesmo_numero():
        numero = randint(1, 100)
        jogador = 'Jogador 1'
        while True:
            print(f'Vez do {jogador}.')
            palpite = input('Diga seu palpite: ')
            try:
                palpite = int(palpite)
            except ValueError:
                print('Palpite inválido, certifique-se de digitar um número inteiro. Exemplos: 1, 10, 100')
                continue
            desistencia(palpite)
            if palpite < 0 or palpite > 100:
                print('O número é gerado entre 1 e 100, caso deseje sair do jogo digite 0.')
                continue
            if palpite == numero:
                print(f'PARABÉNS!!! VOCÊ ACERTOU!')
                print(f'Vitória do {jogador}! ')
                break
            elif palpite < numero:
                print(f'O número é maior que {palpite}!')
            else:
                print(f'O número é menor que {palpite}!')
            jogador = 'Jogador 2' if jogador == 'Jogador 1' else 'Jogador 1'
                
#Função para o modo "2 Jogadores 2 Números"
def numeros_diferentes():
    numero1 = randint(1, 100)
    numero2 = randint(1, 100)
    jogador = 'Jogador 1'
    while True:
        if jogador == 'Jogador 1':
            print(f'Vez do {jogador}')
            palpite_j1 = input('Diga seu palpite: ')
            try:
                palpite_j1 = int(palpite_j1)
            except ValueError:
                print('Palpite inválido, certifique-se de digitar um número inteiro. Exemplos: 1, 10, 100')
                continue
            desistencia(palpite_j1)
            if palpite_j1 < 0 or palpite_j1 > 100:
                print('O número é gerado entre 1 e 100, caso deseje sair do jogo digite 0.')
                continue
            if palpite_j1 == numero1:
                print(f'PARABÉNS!!! VOCÊ ACERTOU!')
                print(f'Vitória do {jogador}! ')
                print(f'O número do Jogador 2 era {numero2}.')
                break
            elif palpite_j1 < numero1:
                print(f'O número é maior que {palpite_j1}!')
            else:
                print(f'O número é menor que {palpite_j1}!')
        elif jogador == 'Jogador 2':
            print(f'Vez do {jogador}')
            palpite_j2 = input('Diga seu palpite: ')
            try:
                palpite_j2 = int(palpite_j2)
            except ValueError:
                print('Palpite inválido, certifique-se de digitar um número inteiro. Exemplos: 1, 10, 100')
                continue
            desistencia(palpite_j2)
            if palpite_j2 < 0 or palpite_j2 > 100:
                print('O número é gerado entre 1 e 100, caso deseje sair do jogo digite 0.')
                continue
            if palpite_j2 == numero2:
                print(f'PARABÉNS!!! VOCÊ ACERTOU!')
                print(f'Vitória do {jogador}! ')
                print(f'O número do Jogador 1 era {numero1}.')
                break
            elif palpite_j2 < numero2:
                print(f'O número é maior que {palpite_j2}!')
            else:
                print(f'O número é menor que {palpite_j2}!')
        jogador = 'Jogador 2' if jogador == 'Jogador 1' else 'Jogador 1'
        
#Mensagem inicial
print('Bem vindo ao jogo da adivinhação!')
print('Tente acertar o número de 1 até 100!')
print('Digite "0" a qualquer momento para parar o jogo.')
print('BOA SORTE!!!')
print('''Escolha o modo de jogo (1) 1 Jogador (2) 2 Jogadores e 1 Número (3) 2 Jogadores e 2 Números (0) Sair
No modo de 2 jogadores e 1 número, os dois jogadores recebem o mesmo número e competem para ver quem acerta primeiro.
No modo de 2 jogadores e 2 números, cada jogador recebe um número e competem para ver quem acerta primeiro o número que recebeu (Existe a possibilidade dos dois jogadores receberem o mesmo número). ''')

#Modos de jogo
um_jogador = 1
um_numero_pra_dois = 2
um_numero_pra_cada = 3

#Escolhendo o modo de jogo
while True:
    modo_jogo = input('Digite o número correspondente ao modo de jogo escolhido: ')
    try:
        modo_jogo = int(modo_jogo)
    except ValueError:
        print('Favor digite um número inteiro.')
        continue
    if modo_jogo == um_jogador:
        modo_solo()
    elif modo_jogo == um_numero_pra_dois:
        mesmo_numero()
    elif modo_jogo == um_numero_pra_cada:
        numeros_diferentes()
    elif modo_jogo == 0:
        print('Encerrando jogo...')
    else:
        print('Opção inválida. Tente novamente.')
print('FIM DE JOGO!')