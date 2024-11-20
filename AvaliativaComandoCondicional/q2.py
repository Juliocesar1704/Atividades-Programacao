try:
# Primeiro pedimos as notas das duas unidades.
    nota1 = float(input("Informe a nota da primeira unidade: "))
    nota2 = float(input("Informe a nota da segunda unidade: "))
# Em seguida declaramos o valor da variavel MD(Media da disiplina).
    MD = float( (2*nota1 + 3*nota2)/5 ) 
# Agora temos a primeira condição estabelecida e nela indicamos que para ser aprovado a media tem que ser maior ou igual a 60 e também deve ser menor ou igual a 100.
    if MD >=60 and MD <=100:
        print("Você está aprovado, sua media foi: ", MD)
# Já aqui nos temso a segunda condição que sera executada caso a primeira não seja atendida. Ela consiste em analisar se a media foi maior ou igual a 20 e menor que 60, e caso a nota do aluno se enquadre ele ira ter que fazer a prova final, ai o codigo vai calcular MD com NAF(Nota da prova final) e mostrar se depois da prova final o aluno esta aprovado ou reprovado.
    elif MD >=20 and MD <60:
        print("Você ira fazer a prova final sua media foi: ", MD)
        NAF = float(input("Informe a nota da prova final: "))
        MDF = (MD + NAF) / 2
        if MDF >=60 and MDF <=100:
            print("Você está aprovado, sua media foi: ",MDF)
        else:
            print("Você está reprovado, sua media foi:", MD)
# Aqui temos a terceira condição que se caso o a MD do aluno for menor que 20 ele estará reprovado direto, sem a chance de fazer a prova final.   
    elif MD <20:
        print("Você está reprovado, sua media foi:", MD)

except ValueError:
    print("Informe apenas numeros")
