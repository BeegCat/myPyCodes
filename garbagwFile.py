'''n= int(input())
ls= set()
for i in range(1, n+1):
    x=input()
    ls.add(x)
    '''
'''for j in range(1,n+1):
    if j '''
'''n=10
for i in range(0, n):
    #print("&", end="^")
    print("W", sep= "yes"+"For sure")'''

'''import datetime

print(datetime.datetime(2002, 8, 9), sep="=")'''


'''
while True:
    ip= input("enter a string")
    if ip=="done" or ip=="Done":
        break
    else:
        continue'''

'''largest=None
print("before", largest)
for i in [2,460,62,300,47,0,19]:
    if largest is None or i>largest:
        largest=i
    print("loop: ", i, largest)
print("largest= ", largest)'''

'''
l= []
k=0
loopvar=0
while True:
    inp=input("enteer a number= ")
    l.insert(k, inp)
    k=k+1
    if inp=="done":
        break

for i in l:
    s=s+i
sum=s

print(l, sep="")
'''
'''
global f
f=101
def prent():
    return print(f)

prent()'''


'''
n=input()

def soln(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    
    two_back=1
    one_back=2
    for i in range(2,x):
        next_num= two_back+one_back
        two_back=one_back
        one_back=next_num

    return one_back

print(soln(n))'''

########################################

arr= ["!", "#", "$", "%", "&", "*", "?", "@", "^"]

nuts= []
bolts= []
i=0
n=int(input())
for i in range(0, n):
    p=input()
    nuts.insert(i, p)

print(nuts)