# Processamento Básico de Imagens

Conjunto de filtros criados em python

## 📌 Índice

- [Contrate e Brilho](#sobre-o-projeto)
- [Redução de Ruídos](#tecnologias-utilizadas)
- [Detecção de Bordas](#instalação)
- [Detecção de Formas e Texturas](#como-usar)
- [Transformações Geométricas](#funcionalidades)
- [Filtros Morfológicos](#autores)

---

## Contraste e Brilho

Definição da função principal que será responsavel pelo ajusto do contraste e brilho que recebe como parametro 
imagem que passará pelo filtho e o novo valor do contrate e brilho.
```python
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

```

Posteriomente, dentro da função utilizo o imagem.size para capturar lagura e altura da imagem passada ara a função, crio uma imagem nova cons as mesmas dimensÕes da passada e carrego os pixels da imagem original e da nova imagem onde
o novo resultado sera salvo.

```python
    largura, altura = imagem.size
    nova_imagem = Image.new("RGB", (largura, altura))
    pixels_originais = imagem.load()
    pixels_novos = nova_imagem.load()
```

Utilizo um laço for aninhado para ir pecorrendo pixel por pixel da imagem e ir fazendo as modificações no brilho e contrante.
Onde pixel a pixel pego o valor original no RGB multiplico esse valor pelo contrate e somo ao valor do brilho. Utilizo o max e min para garantir que os
valores estão entre 0 a 255. E posteriormente salvo esses novos pixels criados para ir formando a nova imagem preocessada pelo filtro
```python
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

```





---

## 🚀 Tecnologias Utilizadas

- Linguagem: `Ex: Python / Java / C / Dart / JavaScript`
- Framework: `Ex: Laravel / Flutter / React`
- Banco de Dados: `Ex: MySQL / PostgreSQL / SQLite`
- Outras ferramentas: `Ex: Docker / Node.js / ANTLR / Tkinter`

---

## ⚙️ Instalação

```bash
# Clone o repositório
git clone https://github.com/seuusuario/nomedoprojeto.git

# Acesse a pasta do projeto
cd nomedoprojeto

# Instale as dependências (se aplicável)
npm install
