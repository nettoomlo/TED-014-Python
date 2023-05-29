def conta_vogais():
    vogais = 'aeiou'
    string = str(input("Digite uma frase: "))
    contador = 0
    for letra in string:
        if letra.lower() in vogais:
            contador += 1
    return contador

resultado = conta_vogais()
print (f"Quantidade de vogais: {resultado}")
