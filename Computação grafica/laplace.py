from PIL import Image

laplaciano = [
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
]


def aplicar_laplace(imagem):
    largura, altura = imagem.size
    pixels = imagem.load()
    nova_imagem = Image.new("L", (largura, altura))
    pixels_novos = nova_imagem.load()

    for x in range(1, largura - 1):
        for y in range(1, altura - 1):
            soma = 0
            for i in range(3):
                for j in range(3):
                    xi = x + i - 1
                    yj = y + j - 1
                    cor = pixels[xi, yj]

                    if isinstance(cor, tuple):
                        cor = int(0.299 * cor[0] + 0.587 *
                                  cor[1] + 0.114 * cor[2])
                    soma += cor * laplaciano[i][j]

            soma = max(0, min(255, soma))
            pixels_novos[x, y] = soma

    return nova_imagem


caminho = "imagem/mesa.jpg"


imagem = Image.open(caminho).convert("RGB")
imagem_bordas = aplicar_laplace(imagem)
imagem_bordas.show()
imagem_bordas.save("imagem/resultado/laplace.jpg")