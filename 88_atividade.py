print("Este código recebe os nomes e notas de 5 alunos, calcula a média geral da turma e lista quem tirou nota abaixo de 7.")

nomes = []
notas = []
soma_notas = 0

for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    
    nomes.append(nome)
    notas.append(nota)
    soma_notas += nota

media = soma_notas / 5
print(f"\n--- Resultados ---")
print(f"Média das notas da turma: {media:.2f}")

print("Alunos com nota menor que 7.0:")
for i in range(5):
    if notas[i] < 7:
        print(f"- {nomes[i]} (Nota: {notas[i]})")