# Pregunta centecimos e imprime cantidad minima de monedas, Fernando Esparza Tinoco, 13 ferbrero 2022 , 13 febrero 2022

#($5, $2, $1, $0.5, $0.2, $0.1

centimos = int(input('Cantidad de centimos: '))

cent = centimos/100

cinco = int(cent//5)
cent = cent%5
dos = int(cent//2)
cent = cent%2
uno = int(cent//1)
cent = cent%1
pcinco = int(cent//.5)
cent = cent%.5
pdos = int(cent//.02)
cent = cent%.02
puno = int(cent//.01)




print('Monedas de 5$: ' + str(cinco))
print('Monedas de 2$: ' + str(dos))
print('Monedas de 1$: ' + str(uno))
print('Monedas de .5$: ' + str(pcinco))
print('Monedas de .2$: ' + str(pdos))
print('Monedas de .1$: ' + str(puno))
