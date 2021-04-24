class supermarket:
    '''this is document string''' # documentation string_
    # __init__ is called automatically when the object is created
    # it is a constructor.it is a special function.it is used to initialize object specific information

    owner = "human"   #class specific variable
    worker  = "Human" #class specific variable
    def __init__(self,brand,price,discount): # formal parameter

        self.brand = brand
        self.price = price
        self.dis = discount

# print(love.__doc__) --> it prints the document of a class

# help(love) --> it gives information about class

# ball = supermarket() # --> object creation
# ball.type = "stumper"
# ball.price = 40

# biscuit = supermarket()
# biscuit.brand = "milk"
# biscuit.price = 10

# print(ball.price) #--> prints price of ball
# print(ball.__dict__) # --> gives all the specification of ball in dictionary

bread = supermarket("xyz",25,25) # actual parameter
print(bread.dis)
biscuit = supermarket("milk",10,3)
print(biscuit.__dict__)
soap = supermarket("wash",10,1)
print(soap.__dict__)

# object specific variable self -->multiple copies will be maintained like brand of biscuit,soap,etc
# class specific variable --> only one copy will be maintained

# print(supermarket.owner) #to access class variable
# print(supermarket.worker)

# I want to change the owner of soap so from human to man so the code below

soap.owner = "man"
# print(soap.owner)
# print(biscuit.owner)

#for gitgit

class bank:

    a = 100
    def deposit(self,amout): # amout is local varibale. it is used in this method only
        print("Amount to be deposited: ",amout)

thiru = bank()
thiru.deposit(500)
thiru.a = 200
print(thiru.a)

'''
Functions - Methods - 3types - 
1 instance method - sample - memory reference - object
   instance variable - object specific variable  - self(keyword)
2 class method - cls is keyword
    - inside the function definition class specific variable only used
    - @classmethod decorator is used
    - cls varible is used
    - can call class name by using class name or object reference
3 static method - utility method 
    - @staticmethod decorator is used
    - it is not object specific and class specific method 
    - local variable are
    
   '''

class student:
    def __init__(self,name,marks):
        self.name = name
        self.mark = marks
    def show(self):
        print(self.name,self.mark)  #instance method
a = student('Thirumalai',100)
a.show()

class love:
    a = 10
    @classmethod
    def display(cls):
        print(cls.a)

s = love()
s.display()

class power:
    @staticmethod
    def powerof(x,y): #static method
        print(x**y)

power.powerof(2,3)
do = power()
do.powerof(2,3)