try:
    
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    if mes < 1 or mes > 12:
        print("Esse mês não é válido!")
    else:
        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        if bissexto == True: 
            anoB = 366
        else:
            if bissexto == False:
                anoB = 365

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

    if dia < 1 or dia > diasM:
        print("Esse dia não é válido!")
    else:
        diaJ = dias_antes + dia
        print("A data",dia,"/",mes,"/",ano, "corresponde ao dia juliano",diaJ, "de", anoB, "dias")

except ValueError:
    print("Informe uma data correta")
