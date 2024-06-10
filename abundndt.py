n= int(input())
#divsrs=[]
for i in range(1,n):
    divsrs=[]
    for j in range(1, i):
        if i%j==0:
            divsrs.append(j)
    if(sum(divsrs)>i):
        print(i)

#print(divsrs)