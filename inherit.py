
# Has a relationship - composition
class engine:
    def __init__(self):
        self.petrol = True
    def start(self):
        print("Smooth......")

class car:
    def __init__(self):
        self.engine = engine()
    def drive(self):
        self.engine.start()

c = car()
c.drive()

#is a relationship - aggregation

class centrabank: #parent class
    def __init__(self):
        self.balance = 1000
        self.ammt = 200
    def deposit(self,amt):
        self.amount = amt
        print("Deposited")
    @staticmethod
    def hate():
        print("Hello")
    @classmethod
    def pop(cls):
        print("lol")
class statebank(centrabank): #child class
    def __init__(self):
        self.amt = 100
        super().__init__() #To access constructor in child class we should use super().__init__()

x = statebank()
x.deposit(100)

print(x.amt) #100
#print(x.ammt) #erro

print(x.ammt)   

#upto this single level inheritance
#----------------------------------------------------------------------------------------------

class one:

    def fun(self):
        print("1st class")
class two(one):
    def love(self):
        print("2nd class")
class three(two):
    def lol(self):
        print("3rd class")

a = three()
a.lol()
a.love()
a.fun()