from PIL import Image
import numpy as np


def filtro_media(imagem_path, tamanho_kernel=3):
    imagem = Image.open(imagem_path).convert("L")
    imagem_np = np.array(imagem, dtype=np.float32)

    altura, largura = imagem_np.shape
    k = tamanho_kernel // 2
    imagem_filtrada = np.zeros_like(imagem_np)

    for y in range(k, altura - k):
        for x in range(k, largura - k):
            vizinhanca = imagem_np[y - k:y + k + 1, x - k:x + k + 1]
            media = np.mean(vizinhanca)
            imagem_filtrada[y, x] = media

    imagem_resultado = Image.fromarray(imagem_filtrada.astype(np.uint8))

    imagem_resultado.show()
    imagem_resultado.save("imagem/resultado/imagem_filtrada_media.jpg")


caminho = "imagem/salPimenta.png"
filtro_media(caminho)
