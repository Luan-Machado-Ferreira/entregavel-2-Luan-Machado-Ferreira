import csv
from modelos import ImagemAnotada


def ler_anotacoes(caminho_csv):
    imagens = {}

    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo, delimiter=",")
        cabecalho = next(leitor, None)

        if cabecalho != ["imagem", "classe_id", "x_min", "y_min", "x_max", "y_max"]:
            raise ValueError("O cabeçalho do CSV está incorreto.")

        for linha in leitor:
            if len(linha) != 6:
                raise ValueError("Cada linha do CSV deve ter 6 campos.")

            nome = linha[0]
            classe_id = int(linha[1])
            x_min = int(linha[2])
            y_min = int(linha[3])
            x_max = int(linha[4])
            y_max = int(linha[5])

            if classe_id != 0 and classe_id != 1:
                raise ValueError("As classes devem ser 0 ou 1.")

            if nome not in imagens:
                imagens[nome] = ImagemAnotada(nome)

            imagens[nome].insere_deteccao(classe_id, x_min, y_min, x_max, y_max)

    if len(imagens) == 0:
        raise ValueError("O CSV não contém anotações.")

    return imagens
