from PIL import Image


def ajutarBrilhoEContrate(imagem, brilho, contraste):

    largura, altura = imagem.size
    nova_imagem = Image.new("RGB", (largura, altura))
    pixels_originais = imagem.load()
    pixels_novos = nova_imagem.load()

    for x in range(largura):
        for y in range(altura):
            r, g, b = pixels_originais[x, y]

            r = int(contraste * r + brilho)
            g = int(contraste * g + brilho)
            b = int(contraste * b + brilho)

            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))

            pixels_novos[x, y] = (r, g, b)

    return nova_imagem


imagem_original = Image.open("imagem1.jpg").convert("RGB")
imagem_ajustada = ajutarBrilhoEContrate(
    imagem_original, brilho=30, contraste=1.3)
imagem_ajustada.show()
imagem_ajustada.save("brilhoEContrate.jpg")
