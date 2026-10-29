print("Esse algoritmo armazena 12 caracteres em um vetor, troca suas posições e apresenta o resultado.")
print()

vetor = []

for i in range(12):
    caractere = input(f"Digite o {i+1}º caractere: ")
    vetor.append(caractere)

print("\nVetor original:", vetor)

for i in range(0, 12, 2):
    vetor[i], vetor[i+1] = vetor[i+1], vetor[i]

print("Vetor modificado:", vetor)