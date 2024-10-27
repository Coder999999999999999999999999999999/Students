#how to create a class
class student:
    #attributes
    #constructors are important for creating objects

    def __init__(self, name, age, classNO, hobby):
        self.name=name
        self.age=age
        self.classNO=classNO
        self.hobby=hobby

    #methods are functions to do something
    def display_student_info(self):
        print("The student's Details are: ")
        print("The name of the student is:", self.name)
        print("The age of the student is", self.age)
        print("Studying in class", self.classNO)
        print("Hobby is", self.hobby)

    def change_name(self):
        print("Please enter your age:")
        self.age=int(input())
        print("What is the name correction?")
        self.name=input()

#Create 2 objects
lev = student("Lev", 11, "year7", "climing wall")
yam = student("Yam", 9, "year5", "football")

uri = student("Uri", 5, "year 1", "dancing")
ron = student("Ron", 48, "year 50", "football")

lev.display_student_info()
lev.change_name()
lev.display_student_info()

yam.display_student_info()
yam.change_name()
yam.display_student_info()

uri.display_student_info()
uri.change_name()
uri.display_student_info()

ron.display_student_info()
ron.change_name()
ron.display_student_info()