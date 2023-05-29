def verifica_primo():
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro: "))
if verifica_primo():
    print(f"{numero} é primo!")
else:
    print(f"{numero} não é primo!")