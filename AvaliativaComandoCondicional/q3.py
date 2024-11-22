import random

    # Sorteia um número entre 1 e 100 esse é o primeiro procedimento 
numero_sorteado = random.randint(1, 100)
intervalo_min = 1
intervalo_max = 100

print('Tente até 4 vezes adivinhar o número sorteado entre 1 e 100, Boa sorte')

    # A primeira tentativa saíra do palpite dito pelo canditado para saber se esta proximo ou longe do numero sortido
print('Primeiro chute : O intervalo é de',  intervalo_min, 'a', intervalo_max)
palpite = int(input('Digite seu palpite: '))
if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)
# Se a caso ele diga o numero 1 será o seu palpite mais um para que ele informe um novo numero acima do que já foi dito 
elif palpite < numero_sorteado:
    intervalo_min = ( palpite + 1 )
    print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 
# Se a caso ele diga o numero 100 e não for ele terá que informar um novo valor a baixo do que já foi dito
else: palpite > numero_sorteado
intervalo_max = palpite - 1
print ('Você errou tenta novamente um numero entr',  intervalo_min, 'a', intervalo_max)


#UMA NOVA OPORTUNIDADE DE TENTAR
palpite = int(input('Digite seu palpite: '))
if palpite == numero_sorteado:
        palpite != numero_sorteado
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)
# Se a caso ele diga o numero 1 será o seu palpite mais um para que ele informe um novo numero acima do que já foi dito 
elif palpite < numero_sorteado:
    intervalo_min =  palpite
    print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 
# Se a caso ele diga o numero 100 e não for ele terá que informar um novo valor a baixo do que já foi dito
else: palpite > numero_sorteado
intervalo_max = palpite - 1
print ('Você errou tenta novamente um numero entr',  intervalo_min, 'a', intervalo_max)


#UMA TERCEIRA OPORTUNIDADE
palpite = int(input('Digite seu palpite: '))
if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)
# Se a caso ele diga o numero 1 será o seu palpite mais um para que ele informe um novo numero acima do que já foi dito 
elif palpite < numero_sorteado:
    intervalo_min = ( palpite + 1 )
    print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 
# Se a caso ele diga o numero 100 e não for ele terá que informar um novo valor a baixo do que já foi dito
else: palpite > numero_sorteado
intervalo_max = palpite - 1
print ('Você errou tenta novamente um numero entre',  intervalo_min, 'a', intervalo_max)


#Por fim uma quarta e última
palpite = int(input('Digite seu último  palpite: '))
if palpite == numero_sorteado:
        print('Você acertou o número tenta agora na mega da virada',  numero_sorteado)
# Se a caso ele diga o numero 1 será o seu palpite mais um para que ele informe um novo numero acima do que já foi dito 
elif palpite < numero_sorteado:
    intervalo_min = ( palpite + 1 )
    print ( 'Você errou tente novamente um numero entre',  intervalo_min, 'a', intervalo_max) 
# Se a caso ele diga o numero 100 e não for ele terá que informar um novo valor a baixo do que já foi dito
else: palpite > numero_sorteado
intervalo_max = palpite - 1
print ('O número correto era: ',  numero_sorteado)
        


