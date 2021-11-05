import sys

N= int(sys.stdin.readline())
Nlist= list(map(int,sys.stdin.readline().split()))
M= int(sys.stdin.readline())
Mlist= list(map(int,sys.stdin.readline().split()))
for  i in Mlist:
    if i in Nlist:
        print("yes",end=" ")
    else:
        print("no",end =" ")