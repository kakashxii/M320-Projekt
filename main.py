from abc import ABC, abstractmethod
from colorama import Fore, Style


import csv


# Define an interface for Teacher and Student

class ITeacher(ABC):
    @abstractmethod
    def add_teacher(self):
        pass

    @abstractmethod
    def display_teacher(self):
        pass

    @abstractmethod
    def search_teacher(self):
        pass

    @abstractmethod
    def delete_teacher(self):
        pass

    @abstractmethod
    def update_teacher(self):
        pass


class IStudent(ABC):
    @abstractmethod
    def add_student(self):
        pass

    @abstractmethod
    def display_student(self):
        pass

    @abstractmethod
    def search_student(self):
        pass

    @abstractmethod
    def delete_student(self):
        pass

    @abstractmethod
    def update_student(self):
        pass


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate


class Teacher(Person, ITeacher):  # Teacher inherits from Person
    def __init__(self, name, birthdate, id_):
        super().__init__(name, birthdate)  # super method
        self.id = id_

    def add_teacher(self, name, birthdate, id_):  # function to add teacher
        teacher = Teacher(name, birthdate, id_)  # object created
        teachers_list.append(teacher)
        print(f"{teacher.name} added to the list!")

    def display_teacher(self, teacher):  # function to display all teachers
        print(
            f"Name: {teacher.name}\nBirthdate: {teacher.birthdate}\nId: {teacher.id}")

    def search_teacher(self, id_):  # function to search teacher
        for i in teachers_list:
            if i.id == id_:
                return i
        print(f"Teacher with id {id_} not found.")

    def delete_teacher(self, id_):  # function to delete teacher
        teacher = self.search_teacher(id_)
        if teacher:
            teachers_list.remove(teacher)
            print(f"{teacher.name} deleted.")
        else:
            print("Teacher not found.")

    def update_teacher(self, id_, name, birthdate):  # function to update teacher
        teacher = self.search_teacher(id_)
        if teacher:
            teacher.name = name
            teacher.birthdate = birthdate
            print(f"{teacher.name} updated.")
        else:
            print("Teacher not found.")


class Student(Person, IStudent):  # student inherits from person

    def __init__(self, name, birthdate, id_):
        super().__init__(name, birthdate)
        self.id = id_

    def add_student(self, name, birthdate, id_):
        student = Student(name, birthdate, id_)

        student_list.append(student)
        print(f"{student.name} added to the list!")

    def display_student(self, student):
        print(
            f"Name: {student.name}\nBirthdate: {student.birthdate}\nId: {student.id}")

    def search_student(self, id_):
        for student in student_list:
            if student.id == id_:
                return student
        print(f"Student with id {id_} not found.")

    def delete_student(self, id_):
        student = self.search_student(id_)
        if student:
            student_list.remove(student)
            print(f"{student.name} deleted.")
        else:
            print("Student not found.")

    def update_student(self, id_, name, birthdate):
        student = self.search_student(id_)
        if student:
            student.name = name
            student.birthdate = birthdate
            print(f"{student.name} updated.")


# create empty lists to store teachers and students
teachers_list = []
student_list = []

# Reading Teachers CSV
with open("teachers.csv", "r") as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    for row in reader:
        name, birthdate, id_ = row
        teachers_list.append(Teacher(name, birthdate, id_))

# Reading Students CSV
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    for row in reader:
        name, birthdate, id_ = row
        student_list.append(Student(name, birthdate, id_))

# menu for console


def menu():
    # Title
    print("\n\033[1;32;47m Welcome to the School Management System \033[m\n")
    # ASCII Art of a School
    print("****************************************************************************************")
    print("____   ____ _   _  ___   ___  _       ____    _  _____  _    ____    _    ____  _____")
    print("/ ___| / ___| | | |/ _ \ / _ \| |     |  _ \  / \|_   _|/ \  | __ )  / \  / ___|| ____|")
    print("\___ \| |   | |_| | | | | | | | |     | | | |/ _ \ | | / _ \ |  _ \ / _ \ \___ \|  _|  ")
    print(" ___) | |___|  _  | |_| | |_| | |___  | |_| / ___ \| |/ ___ \| |_) / ___ \ ___) | |___")
    print("|____/ \____|_| |_|\___/ \___/|_____| |____/_/   \_\_/_/   \_\____/_/   \_\____/|_____|")
    print("\n")
    print("*****************************************************************************************")

    teacher = Teacher('','','')
    student = Student('','','')
    
    while True:
        print(Fore.GREEN + """
        1. Add a teacher
        2. Display all teachers
        3. Search for a teacher by id
        4. Delete a teacher by id
        5. Update a teacher's name and birthdate
        6. Add a student
        7. Display all students
        8. Search for a student by id
        9. Delete a student by id
        10. Update a student's name and birthdate
        11. Exit
        """ + Style.RESET_ALL)
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        choice = int(input("Enter your choice: "))
        print("\n")
        print("\n\033[1;32;47m Output\033[m\n")
        if choice == 1:
            name = input("Enter name: ")
            birthdate = input("Enter birthdate: ")
            id_ = input("Enter id: ")
            teacher = Teacher(name, birthdate, id_)
            teacher.add_teacher(name, birthdate, id_)
        elif choice == 2:
            for teacher in teachers_list:
                teacher.display_teacher(teacher)
        elif choice == 3:
            id_ = input("Enter id: ")
            teacher = teacher.search_teacher(id_)
            if teacher:
                teacher.display_teacher(teacher)
            else:
                print("Teacher not found.")
        elif choice == 4:
            id_ = input("Enter id: ")
            teacher = teacher.search_teacher(id_)
            if teacher:
                teacher.delete_teacher(id_)
            else:
                print("Teacher not found.")
        elif choice == 5:
            id_ = input("Enter id: ")
            name = input("Enter name: ")
            birthdate = input("Enter birthdate: ")
            teacher = teacher.search_teacher(id_)
            if teacher:
                teacher.update_teacher(id_, name, birthdate)
            else:
                print("Teacher not found.")
        elif choice == 6:
            name = input("Enter name: ")
            birthdate = input("Enter birthdate: ")
            id_ = input("Enter id: ")
            student = Student(name, birthdate, id_)
            student.add_student(name, birthdate, id_)
        elif choice == 7:
            for student in student_list:
                student.display_student(student)
        elif choice == 8:
            id_ = input("Enter id: ")
            student = student.search_student(id_)
            if student:
                student.display_student(student)
            else:
                print("Student not found.")
        elif choice == 9:
            id_ = input("Enter id: ")
            student = student.search_student(id_)
            if student:
                student.delete_student(id_)
            else:
                print("Student not found.")
        elif choice == 10:
            id_ = input("Enter id: ")
            name = input("Enter name: ")
            birthdate = input("Enter birthdate: ")
            student = student.search_student(id_)
            if student:
                student.update_student(id_, name, birthdate)
            else:
                print("Student not found.")
        elif choice == 11:
            print("11\033[1;32;47m Thank you for using School Database\033[m\n")
            break
        else:
            print("Invalid choice. Try again.")


menu()
