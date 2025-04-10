from PIL import Image
import numpy as np

def erosao(imagem_bin, tamanho_kernel=3):
    k = tamanho_kernel // 2
    altura, largura = imagem_bin.shape
    erodida = np.zeros_like(imagem_bin)

    for y in range(k, altura - k):
        for x in range(k, largura - k):
            viz = imagem_bin[y - k:y + k + 1, x - k:x + k + 1]
            if np.all(viz == 1):
                erodida[y, x] = 1
    return erodida


def dilatacao(imagem_bin, tamanho_kernel=3):
    k = tamanho_kernel // 2
    altura, largura = imagem_bin.shape
    dilatada = np.zeros_like(imagem_bin)

    for y in range(k, altura - k):
        for x in range(k, largura - k):
            viz = imagem_bin[y - k:y + k + 1, x - k:x + k + 1]
            if np.any(viz == 1):
                dilatada[y, x] = 1
    return dilatada


def abertura(imagem_path, tamanho_kernel=3):
    imagem = Image.open(imagem_path).convert("L")
    imagem_np = np.array(imagem)

    binaria = (imagem_np > 128).astype(np.uint8)

    erodida = erosao(binaria, tamanho_kernel)
    aberta = dilatacao(erodida, tamanho_kernel)

    imagem_final = Image.fromarray((aberta * 255).astype(np.uint8))
    imagem_final.show()
    imagem_final.save("imagem/resultado/imagem_abertura.jpg")
    


caminho = "imagem/celula.jpg"
abertura(caminho)
