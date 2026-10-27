numeros = []

print("Leitura dos 10 números inteiros")
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(valor)

x = int(input("\nDigite o número X: "))

contador = 0
for i in range(len(numeros)):
    if numeros[i] == x:
        contador += 1

print(f"\nO número {x} aparece {contador} vez(es) no vetor.")