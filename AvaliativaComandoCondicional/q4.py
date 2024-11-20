#iniciaremos com um try para avaliar a informação que o testador irá apresentar
try:
# O ano bisexto é aquele divisivel por 4 e 400 todavia não é por 100 sendo assim iremos operar o ano usando divisão por inteiro para identificar
    ano = int(input("Digite um ano"))
    if ( ano % 4 == 0):
        print ( "Este é um ano  bisexto")
    if ( ano % 400 == 0):
        print ( "Este é um ano bisexto")
    if ( ano % 400 or ano % 4 != 0 ):
        print ( "Este não é um ano bisexto")
except ValueError:
    print ( "Digite um ano válido")
