from collections import defaultdict

print("Escreva o nome do aluno e suas respectivas notas")


def media_alunos(dict_nome_nota,pergunta_nome):
    if pergunta_nome in dict_nome_nota.keys():
        return sum(dict_nome_nota)
    else:
        "Aluno não encontrado"

nome_nota = defaultdict(list)

while True:
    nome = input("Coloque o nome do aluno: ") != "":
    if nome == " ":
        break
    else:
    nota_1 = int(input("Nota 1: "))
    nota_2 = int(input("Nota 2: "))
    nome_nota[nome] = (nota_1, nota_2) 


pergunta_nome = input("Digite o nome do aluno para saber a média")
print(media_alunos(dict_nome_nota,pergunta_nome))