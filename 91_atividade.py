print("Esse algoritmo armazena 21 números em um vetor, identifica os ímpares e os organiza em ordem crescente.")

vetor = []
impares = []

for i in range(21):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    
    if numero % 2 != 0:
        impares.append(numero)

if len(impares) == 0:
    print("Todos são pares.")
else:
    print("Existem números ímpares.")
    impares.sort()
    
    print("Números ímpares encontrados:", impares)