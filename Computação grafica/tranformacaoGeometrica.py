from PIL import Image
import numpy as np

def warp_onda(imagem_path, amplitude=20, frequencia=0.05):
    imagem = Image.open(imagem_path).convert("L")
    imagem_np = np.array(imagem)

    altura, largura = imagem_np.shape
    nova_imagem = np.zeros_like(imagem_np)

    for y in range(altura):
        for x in range(largura):
            deslocamento = int(amplitude * np.sin(2 * np.pi * frequencia * y))
            novo_x = x + deslocamento

            if 0 <= novo_x < largura:
                nova_imagem[y, x] = imagem_np[y, novo_x]

    imagem_resultado = Image.fromarray(nova_imagem.astype(np.uint8))

    imagem_resultado.show()
    imagem_resultado.save("imagem/resultado/imagem1_warp_onda.jpg")


caminho = "imagem/imagem1.jpg"
warp_onda(caminho)
