try:
    # Iniciaremos perguntando o dia, mes e ano nessa mesma ordem para desenvolver o programa
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
        # Se a caso coloque algum valor maior que compente a quantidade de meses em um ano será invalid afinal só temos 1 a 12 meses
    if mes < 1 or mes > 12:
        print("Esse mês não é válido!")
        # Agora partiremos para distinguir o ano bissexto do ano convencional para isso utilizaremos o mesmo modelo de calculo da questão anterior
        # COm isso adicionaremos a variavel que sera do ano bissexto ontem terá 366 dia ou se caso não seja apresentaram 365 dias
    else:
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        if bissexto == True: 
            anoB = 366
        else:
            if bissexto == False:
                anoB = 365
        # Agora trataremos o dado informado do dia, mes e ano para determinar o dia juliano que consite em dizer numa escala de 1 a 365 ou 366 o seu correspondente 
        # para isso usamos a seguinte ideia que determinado dia juliano é a soma do dias passados mas o informado
        #  Usamos o mes e seu correspondente de dias para a formular o código seguinte:
    if mes == 1:
        dias_antes = 0
        diasM = 31
    elif mes == 2:
        dias_antes = 31
        diasM = 29 if bissexto else 28
    elif mes == 3:
        dias_antes = 31 + (29 if bissexto else 28)
        diasM = 31
    elif mes == 4:
        dias_antes = 31 + (29 if bissexto else 28) + 31
        diasM = 30
    elif mes == 5:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30
        diasM = 31
    elif mes == 6:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31
        diasM = 30
    elif mes == 7:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30
        diasM = 31
    elif mes == 8:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31
        diasM = 31
    elif mes == 9:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31
        diasM = 30
    elif mes == 10:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30
        diasM = 31
    elif mes == 11:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        diasM = 30
    elif mes == 12:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        diasM = 31
#  para se a caso tivessem informando algum dia maior que as propriedades naturais dos meses, 28,30,31 e 29 dias no ano bissexto
    if dia < 1 or dia > diasM:
        print("Esse dia não é válido!")
    else:
        diaJ = dias_antes + dia
        print("A data",dia,"/",mes,"/",ano, "corresponde ao dia juliano",diaJ, "de", anoB, "dias")

except ValueError:
    print("Informe uma data correta")
