#UTILIZAREMOS O TRY PARA CASO O ALUNO INFORME VALOR INDEVIDO PARA CALCUL0O
try:
# Solicitamos que o aluno coloque as suas notas do periodo, para saber se foi aprovado por média ou será necessário ir para a prova final 
    nota1 = int(input("Informe a nota da primeira unidade: "))
    nota2 = int(input("Informe a nota da segunda unidade: "))

    MD = float( (2*nota1 + 3*nota2)/5 ) 
# partindo  agora para as provas finais utilizaremos tres formulas estipuladas pelo Instituito Federal.
# Iremos utilizar a melhor nota do aluno de acordo com as formulas para informalo que está aprovado ou reprovado 
# O aluno precisa tirar acima de 20 e menor que 60 para a realizar a prova final e na nota final acima de 60 com o máximo da nota 100 ele estará aprovado 
    if MD >= 60 and MD <= 100:
        print("Você está aprovado, sua media foi: ", MD)

    elif MD >= 0 and MD <20:
        print("Você está reprovado, sua media foi:", MD)

    elif MD >=20 and MD <60:
        print("Você ira fazer a prova final sua media foi: ", MD)
        NAF = int(input("Informe a nota da prova final: "))
        
        MFD1 = int((MD + NAF) / 2)

        MFD2 = int(((2*NAF) + (3*nota2)) / 5)

        MFD3 = int(((2*nota1) + (3*NAF)) / 5)


        if MFD1 >= 60 or MFD2 >= 60 or MFD3 >= 60:
            if MFD1 >= MFD2 and MFD1 >= MFD3:
                print("Você está aprovado, sua média foi: ", MFD1)

            elif MFD2 >= MFD1 and MFD2 >= MFD3:
                print("Você está aprovado, sua média foi: ", MFD2)

            else:
                print("Você está aprovado, sua média foi: ", MFD3)

        else:
            print("Você foi reprovado")

        
except ValueError:
    print("Informe apenas numeros")
