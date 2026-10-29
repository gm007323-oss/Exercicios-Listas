print("10 números inteiros para o usuário e armazene-os em um vetor")

numeros = []
soma_impares = 0
multiplicacao_pares = 1  

for i in range(10):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)

for i in range(10):
    if i % 2 != 0:
        soma_impares += numeros[i]
    else:
        multiplicacao_pares *= numeros[i]

print("\n--- Resultados ---")
print(f"1. Soma dos valores nas posições ímpares: {soma_impares}")
print(f"2. Multiplicação dos valores nas posições pares: {multiplicacao_pares}")