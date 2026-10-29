print("Esse algoritmo lê uma frase e substitui espaços, números, acentos e outros caracteres por traços.")
print()

frase = input("Digite uma frase: ")

alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nova_frase = ""

for char in frase:
    if char in alfabeto:
        nova_frase += char
    else:
        nova_frase += "-"

print(f"Frase resultante: {nova_frase}") 