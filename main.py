# Parent class person
class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

# Child class teacher inherits from person

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

class Student(Person):
    def __init__(self, name, birthdate, id_):
        super().__init__(name, birthdate)
        self.id = id_

# Function to add a new student

    def add_student(self, name, birthdate, id_):
        student = Student(name, birthdate, id_) 
        student_list.append(student)
        print(f"{student.name} added to the list!")
    
    # Function to display student details
    def display_student(self, student):
        print(
            f"Name: {student.name}\nBirthdate: {student.birthdate}\nId: {student.id}")

    # Search a student
    def search_student(self, id_):
        for student in student_list:
            if student.id == id_:
                return student
        print(f"Student with id {id_} not found.")

    # Delete a student
    def delete_student(self, id_):
        student = self.search_student(id_)
        if student:
            student_list.remove(student)
            print(f"{student.name} deleted.")
        else:
            print("Student not found.")

    # Update a student
    def update_student(self, id_, name, birthdate):
        student = self.search_student(id_)
        if student:
            student.name = name
            student.birthdate = birthdate
            print(f"{student.name} updated.")
        else:
            print("Student not found.")

# list to hold all students
student_list = []
# creating object of student
student_obj = Student("", "", 0)


class Teacher(Person):
    def __init__(self, name, birthdate, id_):
        super().__init__(name, birthdate)
        self.id = id_
    # Function to add a new teacher

    def add_teacher(self, name, birthdate, id_):
        teacher = Teacher(name, birthdate, id_)
        teachers_list.append(teacher)
        print(f"{teacher.name} added to the list!")
    # Function to display teacher details

    def display_teacher(self, teacher):
        print(
            f"Name: {teacher.name}\nBirthdate: {teacher.birthdate}\nId: {teacher.id}")
    # Search a teacher

    def search_teacher(self, id_):
        for i in teachers_list:
            if i.id == id_:
                return i
        print(f"Teacher with id {id_} not found.")
    # Delete a teacher

    def delete_teacher(self, id_):
        teacher = self.search_teacher(id_)
        if teacher:
            teachers_list.remove(teacher)
            print(f"{teacher.name} deleted.")
        else:
            print("Teacher not found.")
    # Update a teacher

    def update_teacher(self, id_, name, birthdate):
        teacher = self.search_teacher(id_)
        if teacher:
            teacher.name = name
            teacher.birthdate = birthdate
            print(f"{teacher.name} updated.")
        else:
            print("Teacher not found.")


# list to hold all teachers
teachers_list = []
# creating object of teacher
teacher_obj = Teacher("", "", 0)

# function to print menu


def print_menu():
    # Title
    print("\033[1;32;47m Welcome to the School Management System \033[m\n")
    #ASCII Art of a School
    print("____   ____ _   _  ___   ___  _       ____    _  _____  _    ____    _    ____  _____")
    print("/ ___| / ___| | | |/ _ \ / _ \| |     |  _ \  / \|_   _|/ \  | __ )  / \  / ___|| ____|")
    print("\___ \| |   | |_| | | | | | | | |     | | | |/ _ \ | | / _ \ |  _ \ / _ \ \___ \|  _|  ")
    print(" ___) | |___|  _  | |_| | |_| | |___  | |_| / ___ \| |/ ___ \| |_) / ___ \ ___) | |___")
    print("|____/ \____|_| |_|\___/ \___/|_____| |____/_/   \_\_/_/   \_\____/_/   \_\____/|_____|")

    print("\nPlease choose one of the following options:") #code for color
    print("\033[1;34;47m 1. Add a new teacher \033[m")
    print("\033[1;34;47m 2. Display all teachers \033[m")
    print("\033[1;34;47m 3. Search teacher by id \033[m")
    print("\033[1;34;47m 4. Delete teacher by id \033[m")
    print("\033[1;34;47m 5. Update teacher's name and birthdate \033[m")
    print("\033[1;31;47m 6. Exit \033[m")


while True:
    print_menu()
    choice = input("Enter choice: ")
    if choice.isnumeric():
        choice = int(choice)
    else:
        print("Invalid choice, please choose a number from the list.")
        continue
    if choice == 1:
        name = input("Enter teacher name: ")
        birthdate = input("Enter teacher birthdate (dd/mm/yyyy): ")
        id_ = input("Enter teacher id: ")
        if id_.isnumeric():
            teacher_obj.add_teacher(name, birthdate, int(id_))
        else:
            print("Teacher id must be a number")
        
    elif choice == 2:
        if not teachers_list:
            print("No teachers in the list.")
            continue
        print("Teachers list:")
        for teacher in teachers_list:
            teacher_obj.display_teacher(teacher)
    elif choice == 3:
        id_ = input("Enter teacher id to search: ")
        if id_.isnumeric():
            teacher = teacher_obj.search_teacher(int(id_))
        else:
            print("Teacher id must be a number.")
            continue
    elif choice == 4:
        id_ = input("Enter teacher id to delete: ")
        if id_.isnumeric():
            teacher_obj.delete_teacher(int(id_))
        else:
            print("Teacher id must be a number.")
            continue
    elif choice == 5:
        id_ = input("Enter teacher id to update: ")
        if id_.isnumeric():
            name = input("Enter new name: ")
            birthdate = input("Enter new birthdate (dd/mm/yyyy): ")
            teacher_obj.update_teacher(int(id_), name, birthdate)
        else:
            print("Teacher id must be a number.")
            continue
    else:
        print("Goodbye!")
        break
