def encontra_palavras(lista_palavras, letra):
    palavras_encontradas = []
    for palavra in lista_palavras:
        if palavra.startswith(letra):
            palavras_encontradas.append(palavra)
    return palavras_encontradas

palavras = ["python", "programação", "linguagem", "desenvolvimento", "aplicativo"]
letra = "p"
palavras_encontradas = encontra_palavras(palavras, letra)
print(palavras_encontradas)
