print("hello")
# PRIME NUMBER
'''
n=int(input("Enter a number: "))
for i in range (2,n):
    if n % i == 0:
       print ("n is not a prime number ")
       break
    else:
        print("n is a prime number " )  '''


#FACTORIAL
'''
n=int(input("Enter a number : "))
fact= 1
for i in range (1,n+1):
   fact  = fact * i
print ("Factorial= ", fact)    '''

# Break and Continue

for item in range(1,11):
    if item%2==0:
      continue
    print(item)


for item in range(1,11):
    if item%2==0:
      break
    print(item)



# Nested Loop

i=1
while i<=5:
 j=1
 while j<=5:
    print(j, end="")
    j+=1
    print()
    i+=1


for i in range(1,11):
    for j in range(i, i+1):
        print("*", end=" ")
        print()



        #for loop

for i in range(1,10):
    print(i)

name=['Ram','Dam','Shyam','Radha','Mira']
for i in range(len(name)):
    print(i, ':', name[i])


for item in name:
    print(item)
else:
    print("This is Else Part")


#using curly braces{}

intset={23,24,25,26,27,28}
print(intset)

strset={'Ram','Shyam','Dam','Radha','Mira'}
print(strset)

mixedset={333,'Radhika',99.9,6e2}
print(mixedset)

#using the set() function

intset1=set(intset)
print("Set 1:", intset1)

emptyset=set()
print("Set2:", emptyset)

#Add method

name={'Ram','Shyam','Dam'}
print(name)

name.add('Radha')
print(name)

name.clear()
print(name)

#Dictionary

myData={1:'Bangalore',2:'Channai',3:'Pune',4:'Mumbai'}
print(myData)

studentData={
    "name":"Ram",
    "address":"Bangalore",
    "age":20,
    "gender":"Male",
    "profession":"Student"
}

print("Print Student Details:")
print(studentData)
print(studentData["name"])
print(studentData["age"])
studentData["countryName"]="India"
print(studentData)


#Creating a class named Employee
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")


#Creating an object of the Employee class
emp1 = Employee("John Doe", "Software Engineer")
print(emp1.display_info())




#Creating a class named Student, withnout constructor
class Student:
    name = "Radhika"
    age = 20
    grade = "A"

    def display_student_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student1 = Student()
student1.display_student_info()



#Creating a class named Student, with constructor
class Student:
    name = "Radhika"
    age = 20
    grade = "A"

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_student_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


student1 = Student("Ram", 30, "A+")
student1.display_student_info()


#Single Inheritance 
#parent class
class Animal:
    def speak(self):
        print("Animal speaks")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")    

#create an object of the Dog class
dog = Dog()
dog.speak()  # Inherited method from Animal class 
dog.bark()   # Method from Dog class   



#Multilevel Inheritance 

#parent class
class Animal:
    def speak(self):
        print("Animal speaks")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")   

#grandchild class
class DogChild(Dog):
    def eat(self):
        print("DogChild eats")

#create an object of the DogChild class
dogchild = DogChild()
dogchild.speak()  # Inherited method from Animal class
dogchild.bark()   # Inherited method from Dog class
dogchild.eat()    # Method from DogChild  class


#Multiple Inheritance 

#parent class
class pp:
    def ppdata(self):
        print("pp data")

#parent class
class cc:
    def ccdata(self):
        print("cc data")

#child class
class dd(pp, cc):
    def dddata(self):
        print("dd data")

#object of child class
dd_obj = dd()
dd_obj.ppdata()  # Method from pp class
dd_obj.ccdata()  # Method from cc class
dd_obj.dddata()  # Method from dd class


#Compile time Polymorphism (Method Overloading) in Python
class Calculator:
    def multiply(self, a=1,b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

calc = Calculator()
# Calling multiply with two arguments
print(calc.multiply())  # Output: 1
print(calc.multiply(5))

print(calc.multiply(2, 3))  # Output: 6
print(calc.multiply(2, 3, 4))  # Output: 24

#7/7/2026
#Run time Polymorphism (Method Overriding) in Python
class Animal:
    def sound(self):
        return "Animal makes a sound"
class Dog(Animal):
    def sound(self):
        return "Dog barks"
class Cat(Animal):
    def sound(self):
        return "Cat meows"

animals=[Animal(), Dog(), Cat()]
for animal in animals:
    print(animal.sound())  # Output: Animal makes a sound, Dog barks, Cat meows


print(len("Hello"))  # Output: 5
print(len([1, 2, 3, 4]))  # Output: 4
print(max(10, 20))  # Output: 20
print(max("a", "b","z","n"))  # Output: "z"



#functions in Python are defined using the def keyword, followed by the function name and parentheses. Functions can take parameters and return values.

def myFunction():
    print("Hello from myFunction!")

myFunction()

def addNumbers(a, b):
    return a + b

result = addNumbers(5, 3)
print("The sum is:", result)

def RamData(nam="Ram", age=25):
    print("Name:", nam)
    print("Age:", age)

RamData()  # Using default values
RamData("Shyam", 30)  # Providing custom values

#abs() function returns the absolute value of a number
print(abs(-10))  # Output: 10
print(abs(10))   # Output: 10

#all() function returns True if all elements in an iterable are true

kk=[1,2,3,4]
print(all(kk))  # Output: True

kk1=[0,False]
print(all(kk1))  # Output: False

x=10
y=bin(x)
print(y)  # Output: 0b1010



#import ModuleDemo
import ModuleDemo

x=20
y=30
z=ModuleDemo.add(x, y)
print("The sum of", x, "and", y, "is:", z)
p=ModuleDemo.subtract(x, y)
print("The difference of", x, "and", y, "is:", p)

'''--SQL STATEMENT
--DDL
--Create data table'''
'''Create TABLE tblEmployee(
EmpId int Primary Key Identity Not Null,
Name varchar(50) Not Null,
Address varchar(50) Not Null,
EmailId varchar(50) NOt NUll,
PhoneNo varchar(50) Not Null,
Age int Not Null,
Gender varchar(50) Not Null,
CompanyName varchar(50) Not Null,
Salary int Not Null
)

--Alter

--Add
Alter table tblEmployee
Add DeptName varchar(50)

--Change Datatype
Alter table tblEmployee
Alter column DeptName int

--Delete field
Alter table tblEmployee
Drop column DeptName

--Add PK
Alter table tblEmployee
Add Primary Key(EmpId)

--Delete PK
Alter table tblEmployee
Drop Constraint PK__tblEmplo__AF2DBB997CAAC479

--Rename

--rename table name
sp_rename 'tblEmployee','tblEmployeeDemo'

sp_rename 'tblEmployeeDemo','tblEmployee'

--Rename the fields
sp_rename 'tblEmployee.Name','UserName','COLUMN'

--Truncate
Select * from tblEmployee

Truncate table tblEmployee

--Drop

Drop table tblEmployee


--DML
--Insert
Insert into tblEmployee(Name,Address,EmailId,PhoneNo,Age,Gender,CompanyName,Salary)
values('Ram','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Dam','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Shyam','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Rohit','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Biswajit','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Ranjan','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Smruti','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Rupesh','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Suresh','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Rajesh','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000),
('Raman','Bangalore','ram@gmail.com','898989',24,'Male','ITC',34000)

--Update
update tblEmployee set Address='BBSR',EmailId='shyam@gmail.com',CompanyName='TCS' where EmpId=3

--Delete
--Delete single record
Delete from tblEmployee where EmpId=4
--Delete multiple record
Delete from tblEmployee where EmpId IN (5,1,8)
--Delete All record
Delete from tblEmployee



--DQL
--Select
Select * from tblEmployee

Select * from tblEmployee where EmpId=1

Select * from tblEmployee where EmpId>=4
import pypyodbc as odbc

DRIVER_NAME ='SQL SERVER'
SERVER_NAME = 'DESKTOP-16BQH6V\SQLEXPRESS'
DATABASE_NAME = 'ARYANBBSRDB'

connection_string = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER_NAME};
DATABASE={DATABASE_NAME};
Trust_Connection=yes;
"""

conn=odbc.connect(connection_string)
print(conn)'''