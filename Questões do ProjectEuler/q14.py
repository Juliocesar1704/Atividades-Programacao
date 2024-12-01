# Maior sequência de Collatz
N = int(input("Digite um valor: "))
print(N)

while N !=1:

    if N %2 ==0:
        N = N/2
    else:
        N = (3*N) + 1
    print(N) 
