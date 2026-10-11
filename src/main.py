# O OpenCV carrega, salva e exibe as imagens.
import cv2
# A biblioteca os será usada para criar a pasta de resultados.
import os
# Importa a função que lê o CSV e agrupa as detecções por imagem.
from arquivos import ler_anotacoes


# O try permite tratar as exceções no bloco except, ao final.
try:
    # Lê as anotações e recebe um dicionário de objetos ImagemAnotada.
    imagens = ler_anotacoes("dados/anotacoes.csv")
    # exist_ok=True permite usar a pasta caso ela já exista.
    os.makedirs("resultados", exist_ok=True)  # Cria a pasta se ela não existir.

    # sorted organiza os nomes das imagens em ordem alfabética.
    for nome in sorted(imagens):
        # Carrega a imagem original que está na pasta imagens.
        imagem = cv2.imread("imagens/" + nome)
        # imread retorna None quando não consegue abrir a imagem.
        if imagem is None:
            raise ValueError("Não foi possível abrir " + nome)

        # O objeto desta imagem prepara uma cópia com todas as suas caixas.
        resultado = imagens[nome].gerar_imagem_anotada(imagem)
        # Salva o resultado antes de exibir a janela, usando o nome original.
        salvou = cv2.imwrite("resultados/" + nome, resultado)
        # O retorno de imwrite informa se a gravação funcionou.
        if not salvou:
            raise OSError("Não foi possível salvar " + nome)

        # len conta quantas detecções foram desenhadas nesta imagem.
        print(nome, "-", len(imagens[nome].lista_deteccao), "caixas desenhadas.")
        # O título da janela mostra o nome da imagem e a legenda das cores.
        cv2.imshow(nome + " | Classe 0: verde | Classe 1: azul", resultado)

        # O argumento 0 faz waitKey aguardar uma tecla sem limite de tempo.
        tecla = cv2.waitKey(0)
        # ord retorna o código do caractere para compará-lo com a tecla recebida.
        # Se a tecla for diferente de espaço e q, continua esperando nesta imagem.
        while tecla != ord(" ") and tecla != ord("q"):
            tecla = cv2.waitKey(0)

        # Fecha a janela atual depois que espaço ou q for pressionado.
        cv2.destroyAllWindows()
        # q interrompe o laço for; a imagem atual já foi salva.
        if tecla == ord("q"):
            break

except Exception as erro:
    # Mostra no terminal a mensagem da exceção que ocorreu no bloco try.
    print("Erro:", erro)

# Fecha as janelas que ainda estiverem abertas ao finalizar o programa.
cv2.destroyAllWindows()
