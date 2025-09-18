# OOP Example with Employee Classes

#hierarchical inheritance
class Employee:
    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept

class FullTimeEmployee(Employee):
    def __init__(self,name,age,dept,salary):
        super().__init__(name,age ,dept)
        self.salary=salary

    def Display(self):
        print(self.name,self.age,self.dept,self.salary)  
       
class PartTimeEmployee(Employee):
    def __init__(self,name,age,dept,hours):
        super().__init__(name,age,dept)
        self.hourly_rate=5000
        self.hours=hours
        self.salary=self.hourly_rate * self.hours 

    def Display(self):
        print(self.name,self.age,self.dept,self.salary)      

class Intern(Employee):
    def __init__(self,name,age,dept,stipend):
        super().__init__(name,age,dept)
        self.stipend=stipend

    def Display(self):
        print(self.name,self.age,self.dept,self.stipend)      


e1=FullTimeEmployee("John",30,"IT",50000)
e1.Display()

e2=PartTimeEmployee("Doe",25,"HR",20)
e2.Display()

e3=Intern("Jack",21,"Finance",10000)
e3.Display()


#setter and getter methods

class Vehicle:
    pass

class Car(Vehicle):
    def setAttributes(self,model, year, color):
        self.type = "Car"
        self.model = model
        if(year != 0):
            self.year = year   
        else:
            raise ValueError("Year cannot be zero")  
            
        self.color = color

    def getAttributes(self):
        print(self.type,self.model, self.year, self.color)

class Bike(Vehicle):
    def setAttributes(self,model, year, color):
        self.type = "Bike"
        self.model = model
        self.year = year        
        self.color = color

    def getAttributes(self):
        print(self.type,self.model, self.year, self.color)

v1=Car()
v1.setAttributes("Toyota", 2020, "Red")
v1.getAttributes()

v2=Car()
v2.setAttributes("Honda", 2021, "Blue")
v2.getAttributes()


#static methods: workks only on external data

class Bank:
    rate_of_interest = 5.0

    @staticmethod
    def interest(principle, time):
        output=(principle * Bank.rate_of_interest * time) / 100
        print(output)

principle =float(input("Enter principal amount: "))
time=int(input("Enter time in years: "))
Bank.interest(principle, time)


#multi level inheritance

class A:
    def __init__(self):
        print("Class A constructor")
    #parent

class B(A):
    pass
#child

class C(B):
    pass
    #grandchild

c=C() 

#multiple inheritance
class Country:
    x="Pakistan"
class Province:
    x="Punjab"

class District(Province,Country):
    x="Lahore"  

d=District()
print(d.x) #if there is no x in District, it will look for x in Province and then Country


#Encapsulation
#access modifiers: public, private, protected

class Finance:
    def __init__(self):
        self.__revenue = 1000000 #private
        self.__sales= 500000 

    def display(self):
        print(self.__sales)

    def __show(self):
        print(self.__revenue)    

f=Finance()
print(f._Finance__revenue)  #mangling

#print(f.__revenue)  #not accessible, will raise an error
#we can access private variables using methods
f.display() 
#f.__show() #not accessible, will raise an error

