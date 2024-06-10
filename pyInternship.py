'''print("hello world\nhi")

print("AIT\nchikkamangaluru\n\n\n")

a=42
b= "hello"
c= 42.24
d= complex(2, 4)
e= True
print(a,b,c,d,e)

#x= int(input("enter number\n"))
#print("number x= ", x, "was input\n\n")
#print(type(x))

a= int(input("enter value of A"))
b= int(input("enter value of B"))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print("\n\n")

print(a and b, a or b, not a, not b)'''

'''import keyword
print(keyword.kwlist)'''

'''a= int(input())
b= int(input())
c= int(input())
if(a>b and a>c):
    print("a is grtrr")
elif(b>a and b>c):
    print("b is grtr")
else:
    print("c is grtr")'''

'''i=0
while(i!=10):
    print(i)
    i+=2

for j in range(0, 11, 2):
    print(j, end=" ")'''

'''k=10
while(k!=-1):
    #if(k%2!=0):
        print(k)
        k=k-1
'''

'''import time

for i in range(0, 11):
    if i%2==0:
        print(i)
        time.sleep(2)'''




import time

#manufacturing plant 1
temp1= 15.0
pres1= 20.0

#manufacturing plant 2
temp2= 12.0
pres2= 40.0

hour_count=0

while hour_count!=24:
    print("---------------hour=      ---------------\n", hour_count)

    print("|--------MANUFACTURING PLANT 1------|")

    print("enter temp1= \n")
    in_temp1= float(input())
    print("enter pres1= \n")
    in_pres1= float(input())

    if(in_temp1>temp1 and in_pres1<pres1):
        print("machines of plant 1 are functioning as intended.\n")
    else:
        print("----D A N G E R-----")
    #time.sleep(2)

    

    print("|--------MANUFACTURING PLANT 2------|")
    
    print("enter temp2= \n")
    in_temp2= float(input())
    print("enter pres2= \n")
    in_pres2= float(input())
    
    if(in_temp2>temp2 and in_pres2<pres2):
        print("machines of plant 2 are functioning as intended.\n")
    else:
        print("----D A N G E R-----")

    print("######################################################################")
    time.sleep(20)

    hour_count+=1

