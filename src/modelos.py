# O OpenCV fornece as funções para desenhar nas imagens.
import cv2


# Cada objeto desta classe representa uma caixa descrita no CSV.
class Deteccao:
    # __init__ é chamado automaticamente quando criamos um objeto desta classe.
    def __init__(self, classe_id, x_min, y_min, x_max, y_max):
        # self permite guardar os valores no próprio objeto de detecção.
        self.classe_id = classe_id
        self.x_min = x_min
        self.y_min = y_min
        self.x_max = x_max
        self.y_max = y_max

    def desenhar(self, imagem):
        # As cores do OpenCV usam a ordem BGR: azul, verde e vermelho.
        if self.classe_id == 0:
            cor = (0, 255, 0)  # Verde.
        else:
            cor = (255, 0, 0)  # Azul.

        # Desenha diretamente na imagem recebida, entre os dois cantos da caixa.
        # Os pontos usam (x, y), e o 2 indica a espessura da linha em pixels.
        cv2.rectangle(imagem, (self.x_min, self.y_min),
                      (self.x_max, self.y_max), cor, 2)


# Agrupa o nome de uma imagem e todas as detecções que pertencem a ela.
class ImagemAnotada:
    def __init__(self, nome_imagem):
        self.nome_imagem = nome_imagem
        # A lista começa vazia e receberá objetos da classe Deteccao.
        self.lista_deteccao = []

    def insere_deteccao(self, classe_id, x_min, y_min, x_max, y_max):
        # Cria uma detecção e adiciona esse objeto à lista da imagem.
        self.lista_deteccao.append(
            Deteccao(classe_id, x_min, y_min, x_max, y_max)
        )

    def gerar_imagem_anotada(self, imagem):
        # Desenhamos na cópia para preservar a imagem recebida.
        copia = imagem.copy()
        # shape[0] é a altura (linhas), e shape[1] é a largura (colunas).
        altura = imagem.shape[0]
        largura = imagem.shape[1]

        for deteccao in self.lista_deteccao:
            # Confere se os cantos estão ordenados e dentro dos limites da imagem.
            if not (0 <= deteccao.x_min < deteccao.x_max < largura
                    and 0 <= deteccao.y_min < deteccao.y_max < altura):
                raise ValueError("Coordenadas inválidas em " + self.nome_imagem)

            # Cada objeto Deteccao desenha sua própria caixa na cópia.
            deteccao.desenhar(copia)

        # Devolve a imagem com todas as caixas desenhadas.
        return copia
