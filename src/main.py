import cv2
import os
from arquivos import ler_anotacoes


try:
    imagens = ler_anotacoes("dados/anotacoes.csv")
    os.makedirs("resultados", exist_ok=True)

    for nome in sorted(imagens):
        imagem = cv2.imread("imagens/" + nome)
        if imagem is None:
            raise ValueError("Não foi possível abrir " + nome)

        resultado = imagens[nome].gerar_imagem_anotada(imagem)
        salvou = cv2.imwrite("resultados/" + nome, resultado)
        if not salvou:
            raise OSError("Não foi possível salvar " + nome)

        print(nome, "-", len(imagens[nome].lista_deteccao), "caixas desenhadas.")
        cv2.imshow(nome + " | Classe 0: verde | Classe 1: azul", resultado)

        tecla = cv2.waitKey(0)
        while tecla != ord(" ") and tecla != ord("q"):
            tecla = cv2.waitKey(0)

        cv2.destroyAllWindows()
        if tecla == ord("q"):
            break

except Exception as erro:
    print("Erro:", erro)

cv2.destroyAllWindows()
