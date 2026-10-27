numeros = []

print("Leitura dos 12 números inteiros")
print()

for i in range(12):
    valor = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(valor)

print("\nPares:")
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        print(numeros[i])

print()

print("\nÍmpares:")
for i in range(len(numeros)):
    if numeros[i] % 2 != 0:
        print(numeros[i])