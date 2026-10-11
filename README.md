# Entregável 2 — Anotações de imagens com OpenCV

**Autor:** Luan Machado Ferreira

## Objetivo

Criar um visualizador que leia as anotações de `dados/anotacoes.csv`, desenhe as 581 caixas fornecidas nas dez imagens de `imagens/` e exiba uma imagem por vez.

Os resultados são salvos em `resultados/`, mantendo os nomes e as resoluções originais. As imagens de entrada são preservadas. As imagens são processadas em ordem alfabética, e o terminal informa o nome de cada arquivo e sua quantidade de caixas.

## Dependências

- Python 3.
- `opencv-python`, importado como `cv2`, para trabalhar com as imagens.
- Ambiente com suporte a janelas gráficas.

A biblioteca `csv`, usada para ler as anotações, e a biblioteca `os` já acompanham o Python. O pacote `opencv-python` está listado em `requirements.txt`.

## Instruções de execução

Abra o terminal na **raiz do projeto**, onde estão `src/`, `dados/`, `imagens/` e `requirements.txt`.

### Linux ou WSL

Na primeira execução, crie o ambiente virtual, ative-o, instale a dependência e execute:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/main.py
```

Nas próximas execuções, abra um terminal na raiz do projeto e utilize:

```bash
source .venv/bin/activate
python src/main.py
```

#### Aviso de fontes no WSL

Se aparecer `QFontDatabase: Cannot find font directory`, o Qt não encontrou a pasta de fontes. Na raiz do projeto, com a `.venv` ativada, instale as fontes e copie-as para a pasta indicada pelo aviso.

O exemplo abaixo usa Python 3.14. Se o aviso indicar outra versão, substitua `python3.14` nos caminhos pela versão mostrada na mensagem.

```bash
sudo apt install fonts-dejavu-core
mkdir -p .venv/lib/python3.14/site-packages/cv2/qt/fonts
cp /usr/share/fonts/truetype/dejavu/*.ttf .venv/lib/python3.14/site-packages/cv2/qt/fonts/
```

Depois, execute `python src/main.py` novamente. As fontes ficam dentro da `.venv`; se recriar o ambiente, repita a cópia.

### Windows — PowerShell

Na primeira execução, crie o ambiente virtual, instale a dependência e execute:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src\main.py
```

Nas próximas execuções, a partir da raiz do projeto:

```powershell
.\.venv\Scripts\python.exe src\main.py
```

Os comandos do Windows utilizam diretamente o Python do ambiente virtual. Se o comando `py` não estiver disponível, crie o ambiente com `python -m venv .venv` e continue com os comandos seguintes.

Uma execução completa gera dez imagens anotadas em `resultados/`.

## Controles do visualizador

Clique na janela da imagem para que ela receba as teclas.

| Tecla | Ação |
| --- | --- |
| Espaço | Avança para a próxima imagem. |
| `q` | Encerra o programa após salvar a imagem atual. |
| Outras teclas | Mantêm a imagem atual. |

Ao chegar ao fim das imagens, as janelas são fechadas. Se `q` for pressionado antes do fim, são salvas as imagens processadas até a atual.

O título da janela identifica a imagem e apresenta a legenda: **classe 0 em verde** e **classe 1 em azul**. Os IDs das classes são os fornecidos nas anotações.

## Explicação breve das classes

As classes estão definidas em `src/modelos.py`:

- **`Deteccao`:** armazena `classe_id`, `x_min`, `y_min`, `x_max` e `y_max`. O método `desenhar` recebe uma imagem e desenha a caixa correspondente.
- **`ImagemAnotada`:** armazena o nome da imagem e uma lista de objetos `Deteccao`. O método `insere_deteccao` adiciona uma detecção, e `gerar_imagem_anotada` cria uma cópia da imagem e chama o método `desenhar` de cada detecção.
