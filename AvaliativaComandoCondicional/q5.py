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
        dias_do_mes = 31
    elif mes == 2:
        dias_antes = 31
        dias_do_mes = 29 if bissexto else 28
    elif mes == 3:
        dias_antes = 31 + (29 if bissexto else 28)
        dias_do_mes = 31
    elif mes == 4:
        dias_antes = 31 + (29 if bissexto else 28) + 31
        dias_do_mes = 30
    elif mes == 5:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30
        dias_do_mes = 31
    elif mes == 6:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31
        dias_do_mes = 30
    elif mes == 7:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30
        dias_do_mes = 31
    elif mes == 8:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31
        dias_do_mes = 31
    elif mes == 9:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31
        dias_do_mes = 30
    elif mes == 10:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30
        dias_do_mes = 31
    elif mes == 11:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
        dias_do_mes = 30
    elif mes == 12:
        dias_antes = 31 + (29 if bissexto else 28) + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        dias_do_mes = 31

    if dia < 1 or dia > dias_do_mes:
        print("Esse dia não é válido!")
    else:
        dia_juliano = dias_antes + dia
        print("A data",dia,"/",mes,"/",ano, "corresponde ao dia juliano",dia_juliano, "de", anoB, "dias")

except ValueError:
    print("Informe uma data correta")
