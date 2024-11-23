try:
    
    # Sorteia um número entre 1 e 100 esse é o primeiro procedimento 
    # Importar a biblioteca para utilizarmos o randint
    import random
    # A primeira tentativa saíra do palpite dito pelo canditado para saber se esta proximo ou longe do numero sortido
    # O randint é pegar os dois parametros o menor 1 e o maior
    numero_sorteado = random.randint(1, 100)
    intervalo_min = 1
    intervalo_max = 100
    # Agora teremos outro parametro  que será o palpite do jogador 
    print('Tente até 4 vezes adivinhar o número sorteado entre 1 e 100, Boa sorte')
    print('Primeiro chute : O intervalo é de',  intervalo_min, 'a', intervalo_max)
    # Apos seu palpite se ele for maior que as extremidades 1 ou 100 ele ocupara como intervalo maximo ou minimo
    palpite = int(input('Digite seu palpite: '))
    if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)
    # Se ele for menor que o numero sorteado será o intervalo minimo 
    elif palpite < numero_sorteado:
        intervalo_min =  (palpite + 1)
        print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 
    # Se ele for maior que o numero sorteado será o intervalor máximo
    elif palpite > numero_sorteado:
        intervalo_max = (palpite - 1) 
        print ('Você errou tenta novamente um numero entr',  intervalo_min, 'a', intervalo_max)

    palpite = int(input('Digite seu palpite: '))
    if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)
    # Em suma o código a partir de agora será repetido mais 3 vezes que será o limite de apostas
    
    elif palpite < numero_sorteado:
        intervalo_min =  (palpite + 1)
        print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 

    elif palpite > numero_sorteado:
        intervalo_max = (palpite - 1)
        print ('Você errou tenta novamente um numero entre',  intervalo_min, 'a', intervalo_max)

    palpite = int(input('Digite seu palpite: '))
    if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)

    elif palpite < numero_sorteado:
        intervalo_min = ( palpite + 1 )
        print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 

    elif palpite > numero_sorteado:
        intervalo_max = (palpite - 1)
        print ('Você errou tenta novamente um numero entre',  intervalo_min, 'a', intervalo_max)

    palpite = int(input('Digite seu último  palpite: '))
    if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)

    elif palpite < numero_sorteado:
        intervalo_min = ( palpite + 1 )
        print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 

    elif palpite > numero_sorteado:
        intervalo_max = (palpite - 1)
        print ('Você errou o número correto era: ',  numero_sorteado)

except ValueError:
    print("digite apenas numeros")
