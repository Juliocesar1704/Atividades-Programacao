# Múltiplos de 3 ou 5
soma = 0
i = 1
while i <=1000:
    if i %3 == 0 or i % 5 == 0:
        soma = soma + i
    i = i + 1
print(f"A soma dos multiplos de 3 ou 5 é {soma}")
