try:

    nota1 = float(input("Informe a nota da primeira unidade: "))
    nota2 = float(input("Informe a nota da segunda unidade: "))

    MD = float( (2*nota1 + 3*nota2)/5 ) 

    if MD >=60 and MD <=100:
        print("Você está aprovado, sua media foi: ", MD)

    elif MD >=20 and MD <60:
        print("Você ira fazer a prova final sua media foi: ", MD)
        NAF = float(input("Informe a nota da prova final: "))
        MDF = (MD + NAF) / 2
        if MDF >=60 and MDF <=100:
            print("Você está aprovado, sua media foi: ",MDF)
        else:
            print("Você está reprovado, sua media foi:", MD)
    
    elif MD <20:
        print("Você está reprovado, sua media foi:", MD)

except ValueError:
    print("Informe apenas numeros")
