print("Esse algoritmo lê uma frase e um separador, inserindo-o entre cada caractere da frase.")
print()

frase = input("Digite uma frase: ")
separador = input("Digite o separador: ")

resultado = ""

for i in range(len(frase)):
    resultado += frase[i]
    # Adiciona o separador apenas se não for o último caractere
    if i < len(frase) - 1:
        resultado += separador

print(f"Resultado: {resultado}")