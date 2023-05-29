inteiro = int(input("Digite um número inteiro: "))

def calcula_fatorial(inteiro):
    if inteiro == 0:
        return 1
    else:
        return inteiro * calcula_fatorial(inteiro - 1)

fatorial = calcula_fatorial(inteiro)
print(f"O fatorial de {inteiro} é {fatorial}")

