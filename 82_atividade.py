print("Algoritmo que solicita 11 valores")
print()

# Cria uma lista inicializada com 11 posições
valores = [0] * 11

# Solicita e guarda cada valor na respetiva posição da lista
for i in range(len(valores)):
    valores[i] = float(input(f"Informe o {i + 1}º valor: "))

print("\n--- VALORES REGISTADOS ---")

# Exibe os valores guardados com o separador
for i in range(len(valores)):
    print(valores[i])
    print("----------------")