# Tripleto Pitagórico Especial

A = 0
B = 0
C = 0
valorT = 0
# Precisamos encontrar um triplet pitagórico (a, b, c) tal que a + b + c = 1000 
for A in range(1, 1001): 
    for B in range(A + 1, 1001):   
        C = ((1000 - A) - B) 
        # Verificamos se é um triplet pitagórico 
        if A**2 + B**2 == C**2: 
            valorT = (A + B + C)
            print(f"O triplet pitagórico é: A = {A}, B = {B}, C = {C}") 
            print(f"O produto ABC é: {valorT}")
