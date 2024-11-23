try:

    import random

    numero_sorteado = random.randint(1, 100)
    intervalo_min = 1
    intervalo_max = 100

    print('Tente até 4 vezes adivinhar o número sorteado entre 1 e 100, Boa sorte')
    print('Primeiro chute : O intervalo é de',  intervalo_min, 'a', intervalo_max)
    
    palpite = int(input('Digite seu palpite: '))
    if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)

    elif palpite < numero_sorteado:
        intervalo_min =  palpite  
        print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 

    elif palpite > numero_sorteado:
        intervalo_max = palpite 
        print ('Você errou tenta novamente um numero entr',  intervalo_min, 'a', intervalo_max)


    palpite = int(input('Digite seu palpite: '))
    if palpite == numero_sorteado:
        palpite != numero_sorteado
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)
    
    elif palpite < numero_sorteado:
        intervalo_min =  palpite
        print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 

    elif palpite > numero_sorteado:
        intervalo_max = palpite - 1
        print ('Você errou tenta novamente um numero entre',  intervalo_min, 'a', intervalo_max)

    palpite = int(input('Digite seu palpite: '))
    if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)

    elif palpite < numero_sorteado:
        intervalo_min = ( palpite + 1 )
        print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 

    elif palpite > numero_sorteado:
        intervalo_max = palpite - 1
        print ('Você errou tenta novamente um numero entre',  intervalo_min, 'a', intervalo_max)

    palpite = int(input('Digite seu último  palpite: '))
    if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)

    elif palpite < numero_sorteado:
        intervalo_min = ( palpite + 1 )
        print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 

    elif palpite > numero_sorteado:
        intervalo_max = palpite - 1
        print ('Você errou o número correto era: ',  numero_sorteado)

except ValueError:
    print("digite apenas numeros")
