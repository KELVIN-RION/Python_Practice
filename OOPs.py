
#youtube = https://www.youtube.com/playlist?list=PLVkDztYhxUGGsQ3lU605LYKgNoCV-ZBFh


#Class and Object :
'''class Student:
    def __init__(self):
        self.Name = None
        self.Sub_1 = None
        self.Sub_2 = None
        self.Sub_3 = None
        self.Sub_4 = None
        self.Sub_5 = None

    def Total(self):
        total = self.Sub_1 + self.Sub_2 + self.Sub_3 + self.Sub_4 + self.Sub_5
        print("Total Mark of",self.Name, total)

one = Student()
one.Name = "Arun"
one.Sub_1 = 80
one.Sub_2 = 85
one.Sub_3 = 97
one.Sub_4 = 87
one.Sub_5 = 90

two = Student()
two.Name = "Bala"
two.Sub_1 = 90
two.Sub_2 = 85
two.Sub_3 = 97
two.Sub_4 = 85
two.Sub_5 = 92

three = Student()
three.Name = "Carla"
three.Sub_1 = 85
three.Sub_2 = 89
three.Sub_3 = 97
three.Sub_4 = 97
three.Sub_5 = 90

four = Student()
four.Name = "Demon"
four.Sub_1 = 77
four.Sub_2 = 85
four.Sub_3 = 89
four.Sub_4 = 87
four.Sub_5 = 94

five = Student()
five.Name = "Edward"
five.Sub_1 = 75
five.Sub_2 = 82
five.Sub_3 = 94
five.Sub_4 = 89
five.Sub_5 = 100


print(one.Name)
one.Total()

print(two.Name)
two.Total()

print(three.Name)
three.Total()

print(four.Name)
four.Total()

print(five.Name)
five.Total()





#Constructors
class Student:
    def __init__(self, name, sub1, sub2, sub3, sub4, sub5):
        self.Name = name
        self.Sub_1 = sub1
        self.Sub_2 = sub2
        self.Sub_3 = sub3
        self.Sub_4 = sub4
        self.Sub_5 = sub5

    def Total(self):
        total = self.Sub_1 + self.Sub_2 + self.Sub_3 + self.Sub_4 + self.Sub_5
        print("Total Mark of",self.Name, total)

one = Student("Arun", 80, 85, 97, 87, 90)
two = Student("Bala", 90, 85, 97, 85, 92)
three = Student("Carla",85,89,97,97,90) 
four = Student("Demon",77,85,89,87,94)
five = Student("Edward",75,82,94,89,100)

print(one.Name)
one.Total()

print(two.Name)
two.Total()

print(three.Name)
three.Total()

print(four.Name)
four.Total()

print(five.Name)
five.Total()





#Static vs Instance
class Person:

    sleepingtime= 8

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.sleepingtime = 10

person1 = Person("guhan",12)

print(person1.sleepingtime)
print(Person.sleepingtime)


@staticmethod
def Sleep();
    print("person should sleep for", Person.sleepingtime, "hrs")  #Same

    #or
def Sleep(self):
        print("person should sleep for", Person.sleepingtime, "hrs") #Same






#Inheritance
class GrandParent:
    def swim(self):
        print("swimming")

class  Parent(GrandParent):
    def __init__(self):
        self.Networth = 100000

    def Sing(self):
        print("Parent is singing")

class Child(Parent):
    def Dance(self):
        print("Child is dancing")

child1= Child()
print(child1.Networth)


class GrandParent:
    def swim(self):
        print("swimming")

class  Parent:
    def __init__(self):
        self.Networth = 100000

    def Sing(self):
        print("Parent is singing")

class Child(Parent,GrandParent):
    def Dance(self):
        print("Child is dancing")





#Inheritance_2
class Parent:
    def drive(slef,speed):
        print("Parent is driving at the speed of",speed)

class Child(Parent):
    def drive(self,speed):
        super().drive(speed)
        print("child is driving at the speed of",speed-20)

child1 = Child()
child1.drive(50)



#Encapsulation public, private ( used inside that particular class only ), protected (used in a school and a sunclass only)
class School:
    def __init__(self):
        self.Name = "ABC"
        self._Place = "Chennai" #protected ("_")
        self.__Revenue = 500000 #private ("__")
school1= School()
print(school1.Name)
print(school1._Place) #not accessable
print(school1.__Revenue) #not accessable
print(school1._School__Revenue) #cheat accessable
'''


'''
#Getter & Setter (Mainly for Get and Set for private variable)
class Person:
    def __init__(self):
        self.__name = None # accessable
    
    def SetName(self, Value): #Setter, (by same class it is accessable)
        self.__name = Value 

    def GetName(self):#Getter, (by same class it is accessable)
        return self.__name
    
person1= Person()
person1.SetName("Akil")
print(person1.GetName())



class Person:
    def __init__(self):
        self.__name = None # accessable
    
    def SetName(self, Value): #Setter, (by same class it is accessable)
        if len(Value)>20:
            print("Can't set name having characters more than 20")
        else:
            self.__name = Value 

    def GetName(self):#Getter, (by same class it is accessable)
        if self.__name is None:
            return "Please intialize name"
        return self.__name
    
person1= Person()
person1.SetName("Akil")
print(person1.GetName())



class Person:
    def __init__(self):
        self.__name = None # accessable
    
    @property #decorator to use as a variable
    def name(self):#Getter, (by same class it is accessable)
        if self.__name is None:
            return "Please intialize name"
        return self.__name #return is mandetory as it is a getter function
    
    @name.setter
    def name(self, Value): #Setter, (by same class it is accessable)
        if len(Value)>20:
            print("Can't set name having characters more than 20")
        else:
            self.__name = Value 

person1= Person()
person1.name = "vengat"
print (person1.name)



#Polymorphism Compile time (method overload )
class Person:  # here in python it cannot be fully utilized so by default the 2nd def overwrites the 1st def, so by default the 2nd def runs
    def __init__(self,name,age):
        self.Name = name
        self.Age = age

    def Sleep(self,sleepingHours):
        print("Sleeping duration is",sleepingHours)
    
    def Sleep(self,start,end):
        print("Sleeping duration is", end- start)

person1 =  Person("gokul",10)
person1.Sleep(8) #goes to single value input / def 1
person1.Sleep(8,6) #goes to double value input / def 2



#to overcome this below method can be used as a alternate

class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age 

    def Sleep(self,sleepingHours=None, start = None, end = None) :
        if start is not None and end is not None:
           print("Sleeping duration is", abs(end - start))
        else: 
          print("Sleeping duration is" , sleepingHours)



personl= Person("gokul",10)
personl.Sleep(8) # assign for sleepingHours
personl.Sleep(start=2, end=5) # assign for start and end



#Polymorphism Run time (method override)

class Parent:
    def Drive(self):
        print("Parent is driving")

class Child(Parent):
    def Drive(self):
        print("Child is Driving")

obj = None
name= input() #(input is Parent or child)

if name == "Parent":
    obj = Parent()
else:
    obj = Child()

obj.Drive() # here the decision is taken only during the run time
'''



#Abstraction



