import math
n = int(input())
house = list(map(int,input().split(' ')))
temp = []
answer= [math.inf,0]
for i in range(min(house),max(house)+1):
    for i2 in house:
        temp.append(abs(i-i2))
    if answer[0] > sum(temp):
        answer[0],answer[1]=sum(temp),i
    temp.clear()
print(answer[1])




