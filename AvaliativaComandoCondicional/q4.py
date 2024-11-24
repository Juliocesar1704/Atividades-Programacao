#UTILIZAREMOS O TRY PARA CASO O ALUNO INFORME VALOR INDEVIDO PARA CALCUL0O
try:
# Para encontrarmos um ano bissexto é necessaário saber se ele será divisivel por 400 ou 4 e dado essas circustancias não será por 100
    ano = int(input("Digite um ano: "))
    if ( ano % 4 == 0 and ano % 100 != 0) or ( ano % 400 == 0 ):
        print ("Este é um ano  bissexto!")
    else: 
        print("Este não é um ano bissexto!")
   
except ValueError:
    print ( "Digite um ano válido")
