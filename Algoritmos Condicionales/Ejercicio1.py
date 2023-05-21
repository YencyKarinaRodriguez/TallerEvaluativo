#Diseñe un algoritmo que capture dos números, y que realice la suma de dichos números, y mostrar los datos si es el resultado no es negativo.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
addition = number1 + number2

if addition >= 0:
    print("The result of the sum is:", addition)
else:
    print("the result is negative.")
