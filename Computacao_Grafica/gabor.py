from PIL import Image
import numpy as np
import os
from scipy.signal import convolve2d
from scipy import ndimage


def gerar_filtro_gabor(tamanho, lambd, theta, sigma, psi, gamma):
    half = tamanho // 2
    y, x = np.mgrid[-half:half+1, -half:half+1]

    x_theta = x * np.cos(theta) + y * np.sin(theta)
    y_theta = -x * np.sin(theta) + y * np.cos(theta)

    expoente = -(x_theta**2 + (gamma**2) * y_theta**2) / (2 * sigma**2)
    seno = np.cos(2 * np.pi * x_theta / lambd + psi)
    filtro = np.exp(expoente) * seno

    filtro = filtro - np.mean(filtro)
    return filtro / np.sum(np.abs(filtro))


def equalizar_histograma(imagem):
    hist, bins = np.histogram(imagem.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalizado = 255 * cdf / cdf[-1]
    return np.interp(imagem.flatten(), bins[:-1], cdf_normalizado).reshape(imagem.shape)


def aplicar_filtros_gabor(imagem_np, num_orientacoes=4):
    tamanho = 25
    lambd = 12
    sigma = 4.0
    psi = 0
    gamma = 0.5

    orientacoes = np.linspace(0, np.pi, num_orientacoes, endpoint=False)
    resultados = []

    for theta in orientacoes:
        gabor = gerar_filtro_gabor(tamanho, lambd, theta, sigma, psi, gamma)
        resultado = convolve2d(imagem_np, gabor, mode='same', boundary='symm')
        resultados.append(resultado)

    return np.max(np.array(resultados), axis=0)


def aplicar_filtro_gabor_melhorado(imagem_path):
    imagem = Image.open(imagem_path).convert("L")
    imagem_np = np.array(imagem, dtype=np.float32)

    imagem_eq = equalizar_histograma(imagem_np)
    imagem_suavizada = ndimage.gaussian_filter(imagem_eq, sigma=1.0)

    resultado_combinado = aplicar_filtros_gabor(imagem_suavizada)

    resultado_norm = 255 * (resultado_combinado - resultado_combinado.min()) / \
        (resultado_combinado.max() - resultado_combinado.min())

    resultado_final = Image.fromarray(resultado_norm.astype(np.uint8))

    resultado_final.show()
    resultado_final.save("imagem/resultado/impressaoDigital_gabor.jpg")

    return resultado_norm


caminho = "imagem/impressaoDigital.jpg"
aplicar_filtro_gabor_melhorado(caminho)
