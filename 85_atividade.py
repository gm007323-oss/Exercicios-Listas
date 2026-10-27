print("Algoritimo para leitura do nome e idade de 7 pessoas")

nomes = []
idades = []

for i in range(7):
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    nomes.append(nome)
    idades.append(idade)

print("\nPessoas com 18 anos ou mais:")
for i in range(len(idades)):
    if idades[i] >= 18:
        print(nomes[i])