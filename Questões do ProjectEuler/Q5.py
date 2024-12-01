# Menor Múltiplo.
# A questão pede para encontrar o menor número positivo que éuniformemente divisível por todos os números de 1 para 20.
# Fiz uma pequena alteração para ele fazer em escalas de 1 a qualquer numero.

try:

    import math

    i = 1
    r = 1
    num = int(input(" digite o valor da escala de 1 à :"))
    while i <= num:
        r = abs(r * i) // math.gcd(r , i)
        i = i + 1
    print(f"O menor valor divisvel por todod os numeros de 1 a {num} é: {r}")

except ValueError:
    print("Digite um valor válido")
