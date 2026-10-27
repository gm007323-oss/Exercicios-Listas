print("Lista para armazenar os 18 números inteiros")
print()

numeros = []

for i in range(18):
    valor = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(valor)

print("\n--- NÚMEROS EM ORDEM INVERSA ---")

for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i])