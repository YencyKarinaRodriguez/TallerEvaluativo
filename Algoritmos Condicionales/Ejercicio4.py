#Diseña un algoritmo que lea 2 números y visualice si son positivos.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > 0 and number2 > 0:
    print("The numbers are positive.")
else:
    print("The numbers are negative.")