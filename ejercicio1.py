# Pregunta dos numeros y realiza operaciones, Fernando Esparza Tinoco, 13 ferbrero 2022 , 13 febrero 2022

num1 = int(input('ingrese numero uno: '))
num2 = int(input('ingrese numero dos: '))

SUMA = (num1+num2)
RESTA = (num1-num2)
MULTIPLICACION = (num1*num2)
DIVISION = (num1/num2)
DIVISION_ENTERA = (num1//num2)
MODULO = (num1%num2)
POTENCIA = (num1**num2)

print('El resultado de la suma es: ' + str(SUMA))
print('El resultado de la resta es: ' + str(RESTA))
print('El resultado de la multiplicacion es: ' + str(MULTIPLICACION))
print('El resultado de la division es: ' + str(DIVISION))
print('El resultado de la division entera es: ' + str(DIVISION_ENTERA))
print('El resultado del modulo es: ' + str(MODULO))
print('El resultado de la potencia es: ' + str(POTENCIA))