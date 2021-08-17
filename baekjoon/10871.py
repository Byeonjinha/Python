N,X = input().split()
x= list(map(int,input().split()))
x2 =[]
M = int(0)
N = int(N)
X = int(X)
while N>M:
    if  X>x[M]:
        x2.append(x[M])
    M+=1
c= len(x2)
c=int(c)

M = int(0)
while c>M:
    print(x2[M],"",end="")
    M+=1

