a=[]
n= int(input())
r=[]
for i in range(0, n):
    m= input()
    a.insert(i, m)
print(a)

for i in a:
    r.insert(0, i)
print(r)