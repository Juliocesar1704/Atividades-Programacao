#UTILIZAREMOS O TRY PARA CASO O ALUNO INFORME VALOR INDEVIDO PARA CALCUL0O
try:

    #primeiro estabelecer a formula IMC = PESO KG/ALTURA M²
    peso = float(input("Qual seu peso: "))
    altura = int(input ("Informe sua altura em centimetros: "))
    alturaM = altura / 100

    #agora usando valores fornecidos, em questão utilizaremos 2 casa pós virgula  
    imc = float ( peso/(alturaM**2) )
    print ("Seu indice de massa corporal é", round( imc,2 ))

    #Pós apresentado o calculo e identificado o IMC do individuo estabeleceremos o seu valor na classificação da ABESO

    if imc <= 18.5:
        print("Seu IMC está abaixo do normal.")
    elif imc <= 24.9:
        print("Seu IMC está normal. Parabéns, continue com hábitos saudáveis!")
    elif imc <= 29.9:
        print("Seu IMC está com sobrepeso. Vamos praticar atividades físicas e cuidar da alimentação!")
    elif imc <= 34.9:
        print("Seu IMC apresenta Obesidade Grau 1. É hora de procurar acompanhamento com um nutricionista.")
    elif imc <= 39.9:
        print("Seu IMC apresenta Obesidade Grau 2. Procure acompanhamento mais frequente para sua saúde.")
    else:  # Caso em que imc >= 40
        print("Seu IMC apresenta Obesidade Grau 3. Existe risco de doenças graves. Não deixe para amanhã o que pode fazer hoje!")

except ValueError:
    print("Digite um valor válido")
