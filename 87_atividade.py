print("Algoritimo que solicta 8 valores 2x e multiplica cada valor na mesma localizaçaõ")
print()

x = []
y = []

for i in range(9):
   valor = int(input(f"Informe o {i + 1}º número de x: "))
   x.append(valor)

for f in range(9):
   valor = int(input(f"Informe o {f + 1}º número de y: "))
   y.append(valor)

print("\n--- Resultado da Multiplicação (X * Y) ---")
for i in range(9):
    resultado = x[i] * y[i]
    print(f"Posição {i}: {x[i]} * {y[f]} = {resultado}")
