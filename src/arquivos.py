# A biblioteca csv permite ler as linhas e colunas do arquivo de anotações.
import csv
# Importa a classe que reúne as detecções de cada imagem.
from modelos import ImagemAnotada


def ler_anotacoes(caminho_csv):
    # Este dicionário associa cada nome de imagem a um objeto ImagemAnotada.
    imagens = {}

    # O with fecha o arquivo automaticamente ao sair deste bloco.
    with open(caminho_csv, "r", encoding="utf-8") as arquivo:
        # Os campos do CSV são separados por vírgulas.
        leitor = csv.reader(arquivo, delimiter=",")
        cabecalho = next(leitor, None)  # Lê a primeira linha, com os nomes das colunas.

        # Confere os nomes das colunas e a ordem em que devem aparecer.
        if cabecalho != ["imagem", "classe_id", "x_min", "y_min", "x_max", "y_max"]:
            raise ValueError("O cabeçalho do CSV está incorreto.")

        # Cada linha após o cabeçalho representa uma detecção.
        for linha in leitor:
            # São seis campos: nome da imagem, classe e quatro coordenadas.
            if len(linha) != 6:
                raise ValueError("Cada linha do CSV deve ter 6 campos.")

            # O índice 0 indica a primeira coluna, que contém o nome da imagem.
            nome = linha[0]
            # Os valores chegam como texto; int os converte para números inteiros.
            classe_id = int(linha[1])
            x_min = int(linha[2])
            y_min = int(linha[3])
            x_max = int(linha[4])
            y_max = int(linha[5])

            # As anotações deste trabalho aceitam somente as classes 0 e 1.
            if classe_id != 0 and classe_id != 1:
                raise ValueError("As classes devem ser 0 ou 1.")

            # Cria o objeto da imagem apenas na primeira ocorrência desse nome.
            if nome not in imagens:
                imagens[nome] = ImagemAnotada(nome)

            # Adiciona a caixa ao objeto correspondente à imagem desta linha.
            imagens[nome].insere_deteccao(classe_id, x_min, y_min, x_max, y_max)

    # Não há imagens para processar se nenhuma anotação foi lida.
    if len(imagens) == 0:
        raise ValueError("O CSV não contém anotações.")

    # Devolve o dicionário para o main.py acessar as imagens e suas detecções.
    return imagens
