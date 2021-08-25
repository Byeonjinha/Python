import copy
import sys
N ,M = map(int,sys.stdin.readline().split())
x=int(5)
temp=int(0)
P= [(x+1) for x in range(0,N)]
print(P)

for i in range(0,M):
    student1, student2 = map(int,sys.stdin.readline().split())
    if P.index(student1) > P.index(student2):
        temp = copy.deepcopy(P[P.index(student1)])
        P[P.index(student1)] = copy.deepcopy(P[P.index(student2)])
        P[P.index(student2)] = (temp)

print(P)
