l=[]
tmp=[]
n=int(input())
for i in range(0,n):
    x=input()
    l.insert(i, x)

for i in l:
    if i not in tmp:
        tmp.append(i)

print(tmp)