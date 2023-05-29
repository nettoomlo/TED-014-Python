def converte_tempo(tempo_segundos):
    horas = tempo_segundos // 3600
    minutos = (tempo_segundos % 3600) // 60
    segundos = tempo_segundos % 60

    tempo_formatado = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
    return tempo_formatado

segundos = int(input("Digite o tempo em segundos: "))
tempo_formatado = converte_tempo(segundos)
print(tempo_formatado)
