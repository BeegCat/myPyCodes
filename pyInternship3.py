'''name= "vbo"
u=89
op= ["abc"]
print(type(op))
'''
#-------------------------------
'''
class MyClas:
    #print("hello")
    x= "hello"

n=MyClas()
print(n.x)
print(MyClas(x))'''

#------------------------------

'''class Me:
    name= "vbo"
    age= 21
    clg= "ait"
    deg= "ec"
    tst= int(input("enter a number"))
    loc= "beekanahalli"

p= Me()
print(p.name, p.age, p.deg)
#print(Me.tst)
print("value entered is= ", p.tst)
print(p.loc)'''

#-------------------------------

'''class tes:
    def helo():
        x= input("enter your  name= ")
        print("this is your name= ", x)

tes.helo()'''

#-----------------------------
'''
class Persom:
    def talk():
        print("i can talk")

humn= Persom()
humn.talk()
'''
#-----------------------------
''' 'self;' is only needed when we are using a reference variable like x= Animal(). if calling directly from class then not needed.. like in Animal.run()
class Animal:
    nmae= "abc"
    clr= "red"

    def run(self):
        print("im running")
    
    def prRed(self):
        print(Animal.clr)
    

x= Animal()
print(x.nmae)
print(x.clr)
x.run()
x.prRed()'''

#---------------------------

'''class Animal:
    def run():
        print("i cab run")

Animal()
Animal.run()'''

#----------------------------

#one class can have only one constructor
'''
class College:
    def __init__(self, var1, var2):
        #self.var1= 90
        #self.var2= 10
        self.sm= var1+var2
        print(self.sm)

m= College(90,10)
#print(m)
'''
#-----------------------------

'''class College:
    def __init__(self, name, branch):
        self.name= name
        self.branch= branch

m= College("ait", "ece")
print(m.name, m.branch)
'''

'''
class College:
    def __init__(self, name, branch):
        self.name= name
        self.branch= branch

    def display(self):
        print(self.name, self.branch)
m= College("ait", "ece")
m.display()
#print(m.name, m.branch)'''

#-----------------------------
'''
class Adder:
    def __init__(self, x, y):
        self.x= x
        self.y= y


    def addMeth(self):
        print(self.x+self.y)

x= Adder(30,14)
x.addMeth()'''

#------------------------------------

'''
class Account:
    #owner= "abc"
    #balance= 120000

    def __init__(self, owner, balance):
        self.owner= owner
        self.balance= balance


    def deposit(self, depamt):
        #m= int(input("enter a value= "))
        print("\nyouu hhave deposited", depamt, "amount of rupees\n")
        self.balance= self.balance+depamt
        print("new blance= \n", self.balance)


    def withdraw(self, wthdrwamt):
        #n= int(input("enter amt to withdraw= "))
        print("amt entered is", wthdrwamt)
        if self.balance>wthdrwamt:
            self.balance= self.balance-wthdrwamt
        else:
            print("\nlow balance!! try again!No amt has been deducted.\n")
        print("new blance= \n", self.balance)

    def prtDetails(self, owrnm, owrblc):
        print(self.owner, self.balance)

        
t= Account("abc", 120000)

print("welcome!!\nusername=", t.owner,"\nacc balance=", t.balance)
ch= input("\nenter a choice:\n1.DEPOSIT\n2.WITHDRAW \n")
if (ch== "1"):
    t.deposit(5000000)
elif ch== "2":
    t.withdraw(5000)
else:
    print("\nprovide a valid input.\n")

#t.deposit(200)

'''
#-----------------------------------------------
#single inheritance
'''
class College:
    def details(self):
        print("ait chikmaglur")

class Student(College):
    pass

x= College()
x.details()'''
#-------------------------------------------------
'''
class Dept:
    def __init__(self, branch, hod):
        self.branch= branch
        self.hod= hod

class Collg(Dept):
    print("hello\n")
    
d= Collg("abc", "def")
print(d.branch, d.hod)
'''
#-------------------------------------------------

#multiple inheritance
'''
class Jump:
    def jump(self):
        print("can jump")

class Swim:
    def swim(self):
        print("can swim")

class Amph(Jump, Swim):
    pass

frog= Amph()
frog.jump()
frog.swim()
'''

'''
class A:
    def summ(self, m, n):
        return m+n
    
class B:
    def mull(self, m, n):
        return m*n
    
class K(A, B):
    pass


p=K()
print(p.summ(3,4))
print(p.mull(7,929))
'''
#-------------------------------------------

#multilevel inheritance

#------------------------------
#polymorphism
'''
class Rect:
    def area(self, a, b):
        return a*b
    
class Square:
    def area(self, a):
        return a*a
    
rc1= Rect()
sq1= Square()
ls= [rc1, sq1]

print(rc1.area(3,4))
print(sq1.area(8))
'''
#--------------------------
'''
class Cat:
    def sound(self):
        print("meaow")

class Duck:
    def sound(self):
        print("quaack")

c1= Cat()
d1= Duck()

def spk(animl):
    animl.sound()

spk(c1)
spk(d1)
'''
#----------------------------
#encapsulation
'''
class Person:
    def __init__(self, name, phon, age):
        self.name= name  #public
        self._phon= phon #protected
        self.__age= age #private

    def get(self):
        print(self.__age)

    def sett(self, num):
        self.__age= num
        return self.__age

p1= Person("dw", 2345, 21)
print(p1.name)
print(p1._phon)
p1.get()
print(p1.sett(50))'''

#---------------------------
#abstraction

'''
from abc import ABC, abstractmethod

class Vehicle(ABC):    #atleast one method must be decorated with "@"
    @abstractmethod
    def start(self):
        pass

    #@abstractmethod
    def color(self):
        pass

class Scooty(Vehicle):
    def start(self):
        print("self starts")

    def color(self):
        print("black")
v1= Scooty()
v1.start()
v1.color()
'''

#---------------------------