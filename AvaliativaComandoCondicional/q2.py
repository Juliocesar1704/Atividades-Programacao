try:

    nota1 = float(input("Informe a nota da primeira unidade: "))
    nota2 = float(input("Informe a nota da segunda unidade: "))

    MD = float( (2*nota1 + 3*nota2)/5 ) 

    if MD >=60 and MD <=100:
        print("Você está aprovado, sua media foi: ", MD)

    elif MD >=0 and MD <20:
        print("Você está reprovado, sua media foi:", MD)

    elif MD >=20 and MD <60:
        print("Você ira fazer a prova final sua media foi: ", MD)
        NAF = float(input("Informe a nota da prova final: "))
        MFD1 = (MD + NAF) / 2
        MFD2 = (2*NAF) + (3*nota2) / 5
        MFD3 = (2*nota1) + (3*NAF) / 5


        if MFD1 >=60 and MFD1 <=100 and MFD1 >MFD2 and MFD1 >MFD3:
            print("Você está aprovado, sua media foi: ", MFD1)

        elif MFD2 >=60 and MFD2 <=100 and MFD2 >MFD1 and MFD2 >MFD3:
            print("Você está aprovado, sua media foi: ", MFD2)

        elif MFD3 >=60 and MFD3 <=100 and MFD3 >MFD1 and MFD3 >MFD2:
            print("Você está aprovado, sua media foi: ", MFD3)
        
        else:
            print("Você foi reprovado")
        
except ValueError:
    print("Informe apenas numeros")
