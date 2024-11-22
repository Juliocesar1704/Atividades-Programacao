try:
    dia = int(input("Informe o dia: "))
    mes = int(input("Informe o mês: "))
    ano = int(input("Informe o ano: "))

    dias_em_j = 0


    if (ano % 4 == 0) or (ano % 400 == 0):
        if mes == 2:
            dia == 29
        
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                dia == 31
            else:
                dia == 30
                print("Esse é um ano bissexto.")
    
            if mes >1:
                dias_em_j = dias_em_j + 31
            if mes >2:
                dias_em_j = dias_em_j + 29
            if mes >3:
                dias_em_j = dias_em_j + 31
            if mes >4:
                dias_em_j = dias_em_j + 30
            if mes >5:
                dias_em_j = dias_em_j + 31
            if mes >6:
                dias_em_j = dias_em_j + 30
            if mes >7:
                dias_em_j = dias_em_j + 31
            if mes >8:
                dias_em_j = dias_em_j + 31
            if mes >9:
                dias_em_j = dias_em_j + 30
            if mes >10:
                dias_em_j = dias_em_j + 31
            if mes >11:
                dias_em_j = dias_em_j + 30
            if mes ==12:
                dias_em_j = dias_em_j + 31

                print("Dias em juliano é :", dias_em_j)

    elif (ano % 100 != 0):
            if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                dia == 31
            else:
                dia == 30
                if mes == 2:
                    dia == 28

                    print("Esse não é um ano bissexto.")

            if mes >1:
                dias_em_j = dias_em_j + 31
            if mes >2:
                dias_em_j = dias_em_j + 28
            if mes >3:
                dias_em_j = dias_em_j + 31
            if mes >4:
                dias_em_j = dias_em_j + 30
            if mes >5:
                dias_em_j = dias_em_j + 31
            if mes >6:
                dias_em_j = dias_em_j + 30
            if mes >7:
                dias_em_j = dias_em_j + 31
            if mes >8:
                dias_em_j = dias_em_j + 31
            if mes >9:
                dias_em_j = dias_em_j + 30
            if mes >10:
                dias_em_j = dias_em_j + 31
            if mes >11:
                dias_em_j = dias_em_j + 30
            if mes ==12:
                dias_em_j = dias_em_j + 31

                print("Dias em juliano é :", dias_em_j)
            

except ValueError:
    print("Informe a data correta")
