try:
    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mês: "))
    ano = int(input("Informe o ano: "))

    if (ano % 4 == 0) or (ano % 400 == 0):
        if mes == 2:
            dia == 29
        
        else:
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                dia == 31
            else:
                dia == 30

    else:
        if (ano % 100 != 0):
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                dia <= 31
            else:
                dia <= 30
                if mes == 2:
                    dia <= 28


except ValueError:
    print("Informe a data correta")
