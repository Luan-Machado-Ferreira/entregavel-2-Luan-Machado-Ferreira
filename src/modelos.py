import cv2


class Deteccao:
    def __init__(self, classe_id, x_min, y_min, x_max, y_max):
        self.classe_id = classe_id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def desenhar(self, imagem):
        if self.classe_id == 0:
            cor = (0, 255, 0)
        else:
            cor = (255, 0, 0)

        cv2.rectangle(imagem, (self.x_min, self.y_min),
                      (self.x_max, self.y_max), cor, 1)


class ImagemAnotada:
    def __init__(self, nome_imagem):
        self.nome_imagem = nome_imagem
        self.lista_deteccao = []

    def insere_deteccao(self, classe_id, x_min, y_min, x_max, y_max):
        self.lista_deteccao.append(
            Deteccao(classe_id, x_min, y_min, x_max, y_max)
        )

    def gerar_imagem_anotada(self, imagem):
        copia = imagem.copy()
        altura = imagem.shape[0]
        largura = imagem.shape[1]

        for deteccao in self.lista_deteccao:
            if not (0 <= deteccao.x_min < deteccao.x_max < largura
                    and 0 <= deteccao.y_min < deteccao.y_max < altura):
                raise ValueError("Coordenadas inválidas em " + self.nome_imagem)

            deteccao.desenhar(copia)

        return copia
