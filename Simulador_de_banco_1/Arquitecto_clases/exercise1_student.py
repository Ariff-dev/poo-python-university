# Ejemplo 1: Escuela
# Imagina que queremos modelar a un estudiante en un curso. Podríamos tener una clase llamada Student que tenga variables de instancia para:
# nombre
# dirección de correo electrónico
# calificación actual
# entre otros. 
# Cada objeto Student que creemos a partir de esta clase tendría su propio conjunto de estas variables de instancia, y los valores asignados a las variables de instancia serían diferentes para cada estudiante.

class Student():
    def __init__(self, name, email, grade, classGroup) -> None:
        self.name = name
        self.email = email
        self.grade = grade
        self.classGroup = classGroup
    
    def showStudent(self):
            print(f""" 
                    1.Nombre: {self.name}
                    2.Email: {self.email}
                    3.Calif:{self.grade}
                    4.Grupo:{self.classGroup}
                """)
    def changeGrade(self, newGrade):
        self.grade = newGrade
        return self.grade
    
eduardo = Student("Eduardo", "edu@example.com", 9, "3A")

eduardo.showStudent()
nuevo_grado = eduardo.changeGrade(10)
eduardo.showStudent()