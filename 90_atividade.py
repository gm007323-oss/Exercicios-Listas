print("O algoritmo solicita um número inteiro e conta quantas vezes um número aparece em um vetor de 32 posições.")
print()

X = int(input("Digite o número X que deseja procurar: "))

vetor = []
contador = 0

for i in range(32):
    numero = int(input(f"Digite o {i+1}º número para o vetor: "))
    vetor.append(numero)

for numero in vetor:
    if numero == X:
        contador += 1

print(f"O número {X} apareceu {contador} vez(es) no vetor.")