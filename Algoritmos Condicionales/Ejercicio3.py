#Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso, nota definitiva, el nro de clases en el semestre y el número de las fallas. En el caso de que las fallas superen el 30% del número de clases se debe mostrar la nota que no aprobó y se calificara cero(0)

name_apprentice = input("Enter the name of the apprentice: ")
name_course = input("Enter the name of the course: ")
note_final = float(input("Enter the final note: "))
number_class = int(input("Enter the number of classes in the semester: "))
number_failures = int(input("Enter the number of failures: "))
percentage_failures = number_class * 0.30

if number_failures >= percentage_failures:
    note_final = 0
    print("Not approved. your note is zero (0).")
    print("Name apprentice:", name_apprentice)
    print("Name course:", name_course)
    print("Note final:", note_final)
    print("Number of classes in the semester:", number_class)
    print("Number failures:", number_failures)

else:
    print("Name apprentice:", name_apprentice)
    print("Name course:", name_course)
    print("Note final:", note_final)
    print("Number of classes in the semester:", number_class)
    print("Number fauilures:", number_failures)