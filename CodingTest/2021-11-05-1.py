import sys
from itertools import combinations
n , m = map(int, sys.stdin.readline().split())
k = sys.stdin.readline().strip().split(" ")
answer = []
for i in list(combinations(k,2)):
    if i[0]!=i[1]:
        answer.append(i)
print(len(answer))


