'''temp_thr= 20
pres_thr= 35

#count=0
while(1):
    temp_in= float(input("enter temp= "))
    pres_in= float(input("enter pres= "))

    if(temp_in>temp_thr):
        print("------threshold values exceeded, aborting process.-----")
        break
        '''
#-------------------
'''while(1):
    temp_in= float(input("enter temp"))
    pres_in= float(input("enter pres"))
    pwr_in= bool(input("enter pwr"))

    if(pwr_in):
        print("aborting process")
        break'''
#--------------
'''s= input("enter str= ")
print(s[0:len(s)-1:2])
print(s[::-1])'''
#----------------------
'''
l=[]
for i in range(0, 11):
    x= input("enter some value= ")
    l.append(x)
print(l)
#print(l.remove())
print(l.pop())
#print(l.)'''
#----------------------
'''
t=('a', 34, 42.0)
''''''for i in range(0,5):
    x= input("enter values= ")
    t.append(x)''''''

print(t)
print(t[::-1])'''

#---------------------
'''
x=set()
x.add("e")
print(x)
for i in range(0,4):
    m= input("enter some value= ")
    x.add(m)
print(x)
print(type(x))'''

#-----------------------

'''s= {'rre', 32}

#s.append(100)
print(s)
f= frozenset(s)
print(type(f))'''

#-----------------------

'''dct= {}
print(type(dct))
dct= {23:"hello", 32:3, 42:54.0, 33:complex(2, 4), 44:True}
print(dct)
dct["sdd"]= 43
print(dct)
print(dct.values())

print("\n\n\n", dct.keys())''' 
#-----------------

#x= input("enter an integer= ")
#print("x"+2)
# 
'''l=[1, 3, 45]
try:
    print(l[1])
    #print("\n\n",l[1],"\n\n")
except (IndexError, ZeroDivisionError):
    print("\n\nan index value out of range was attempted to be accessed. Index error occured.\n\n")
else:
    print("ok")
finally:
    print("this should always execute")'''
#-----------------------------------

'''a= int(input("enter number"))


for i in range(1, 11):
    print(a,"*",i,"=",a*i)
'''

'''
import random
x=[]
otp= random.randrange(111111, 999999, 1)
#for i in range(000000, 999999):

for i in range(0, len(otp)-1):
    x.append(otp[i])
print(x,sep=" ")

'''

#----------------------------
'''
def arit(a,b):
    #a= int(input("enter value of a= "))
    #b= int(input("ennter valur of b= "))
    op= input("enter the oprtr= ")

    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op== "/":
        return a/b
    elif op== "//":
        return a//b
    elif op== "%":
        return a%b
    else:
        exit()

m= int(input("eter value of a= "))
n= int(input("enter value of b= "))
print(arit(m,n))'''
#print(arit(a,b)) w/o p w r, w p w r, w/o p w/o r, w/o p w r

'''
def arit():
    a= int(input("enter value of a= "))
    b= int(input("ennter valur of b= "))
    op= input("enter the oprtr= ")

    if op=="+":
        return a+b
    elif op=="-":
        return a-b
    elif op=="*":
        return a*b
    elif op== "/":
        return a/b
    elif op== "//":
        return a//b
    elif op== "%":
        return a%b
    else:
        exit()

#m= int(input("eter value of a= "))
#n= int(input("entelue of b= "))
print(arit())'''

#----------------------------
'''
def art(*args_name):
    for i in args_name:
        print(i+10)
    print(args_name)

art(2, 13, 44, 12, 42)
'''
'''
def arith(*m):
    l=[]
    for i in m:
        l.append(i+10)
   # print(m)
    return l

print(arith(2,5,35,29))'''
#----------------------------
'''
def pt(**kwargs_name):
    print("\n")
    for k,v in kwargs_name.items():
        print("key= ", k, "|", "value= ", v, "\n")

pt(a=30, b=0.219, c= "hello", d="39")
'''
#---------------------------
'''

def arith(*m):
    l=[]
    for i in m:
        l.append(i+10)
   # print(m)
    return l

print(arith(2,5,35,29))

'''
#-----------------------------

def pt(**kwargs_name):  #kwargs_name converts the params in line 212 into key value pairs. until then they are nor key value pairs.
    print("\n")
    for k,v in kwargs_name.items():
        print("key=", k, "values= ", v, "\n")

pt(a=30, b=0.219, c= "hello", d="39")

#------------------------------

