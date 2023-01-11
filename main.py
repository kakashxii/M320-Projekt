
#create class Person
class Person:
    #constructor
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

#create class Teacher
class Teacher(Person):
    #constructor
    def __init__(self, name, birthdate, id,):
        super().__init__(name, birthdate)
        self.id = id

    #function to create and add new teacher
  
    def accept(self, Name, Birthdate, Id):
        #use input method to take input from user
        ob = Teacher(Name, Birthdate, Id)
        #append object
        ls.append(ob)
    
    #function to display details teacher
    def display(self, ob):
        print("Name: ", ob.name)
        print("Birthdate: ", ob.birthdate)
        print("Id: ", ob.id)
        print("\n")

    #search function
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].id == rn):
                return i

    #delete function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
    
    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        number = No
        ls[i].id = number

#create list with all teachers
ls = []

#create object teacher
obj = Teacher('', 0, 0, 0)

print("\nOperation used, ")
print("\n1.Accept Teacher details\n2.Display Teacher Details\n3.Search Details of a Teacher\n4.Delete Details of Student\n5.Update Teacher Details\n6.Exit")

obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)


print("\n")
print("\nList of Teachers\n")
for i in range(ls.__len__()):
    obj.display(ls[i])

print("\n Teacher Found, ")
s = obj.search(2)
obj.display(ls[s])