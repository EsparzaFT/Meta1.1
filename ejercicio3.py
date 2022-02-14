# Pregunta cantidad de segundo e imprime dias, horas, minutos, segundos, Fernando Esparza Tinoco, 13 ferbrero 2022 , 13 febrero 2022

sec = int(input('Ingresa los segundos: '))

dias = int(sec/86400)
sobDias = sec%86400
horas = int(sobDias/3600)
sobHoras = sobDias%3600
minutos = int(sobHoras/60)
segundos = int(sobHoras%60)

print('Dias: ' + str(dias) + ' Horas: ' + str(horas) + ' Minutos: ' + str(minutos) + ' Segundos: ' + str(segundos))