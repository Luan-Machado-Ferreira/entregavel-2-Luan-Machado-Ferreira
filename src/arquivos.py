import csv

lista_anotacoes = []

with open("dados/anotacoes.csv","r") as anotacoes:
    anotacoes_csv = csv.reader(anotacoes, delimiter = ",")
    for linha in anotacoes_csv:
        lista_anotacoes.append(linha)

print(lista_anotacoes)