print("Esse algoritmo lê uma frase e conta as vogais, consoantes e outros caracteres presentes nela.")
print()

frase = input("Digite uma frase: ")

qtd_vogais = 0
qtd_consoantes = 0
qtd_outros = 0

vogais = "aeiouAEIOU"
consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

for char in frase:
    if char in vogais:
        qtd_vogais += 1
    elif char in consoantes:
        qtd_consoantes += 1
    else:
        qtd_outros += 1

print(f"Vogais: {qtd_vogais}")
print(f"Consoantes: {qtd_consoantes}")
print(f"Outros caracteres: {qtd_outros}")