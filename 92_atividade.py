print("Esse algoritmo armazena valores em dois vetores, identifica os números comuns e os apresenta em ordem decrescente.")

vetor1 = []
vetor2 = []
comuns = []

print("--- Primeiro Vetor (10 valores) ---")
for i in range(10):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor1.append(valor)

print("--- Segundo Vetor (12 valores) ---")
for i in range(12):
    valor = int(input(f"Digite o {i+1}º valor: "))
    vetor2.append(valor)

for valor in vetor1:
    if valor in vetor2 and valor not in comuns:
        comuns.append(valor)

if len(comuns) == 0:
    print("\nNão há valores comuns entre os dois vetores.")
else:
    comuns.sort(reverse=True)
    
    print("\nValores comuns em ordem decrescente:", comuns)