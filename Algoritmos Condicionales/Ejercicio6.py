#Crear un algoritmo que lea el nombre de un empleado, su salario básico por hora, el nro. de horas trabajadas en un mes. Se requiere lo siguiente:
#✓ Calcular su salario mensual adicionalmente el subsidio de transporte, si su sueldo es mayor o igual a 2 salarios mínimos legal vigente. Tener en cuenta que el salario mínimo es $1030.000 y el subsidio por transporte es $70.000 .
#✓ Mostrar: el nombre del empleado, su salario mensual, el subsidio de transporte y su sueldo neto.

employee = input("Enter your name: ")
salary_hour = float(input("Enter your hourly wage: "))
hours_worked = int(input("Enter the number of hours worked in the month: "))
salaryMinium = 1030000
susidyTransport = 70000
salary = salary_hour * hours_worked
addSubsidy = 2060000
salaryAddSubsidy = salary + susidyTransport

if salary >= addSubsidy:
    print(f"\n\nYour name is: {employee}\nYour hourly wage is: {salary_hour}\nNumber of hours worked: {hours_worked}\nHis total salary is: {salaryAddSubsidy}")
    
else:
    print(f"\n\nYour name is: {employee}\nYour hourly wage is: {salary_hour}\nNumber of hours worked: {hours_worked}\nHis total salary is: {salary}")