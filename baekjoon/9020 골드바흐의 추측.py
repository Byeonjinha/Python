from itertools import combinations
import sys



def solution(n):                    # n 이 주어지면 n 이하의 소수를 출력
    a = [True] * (n + 1)
    m = int(n**0.5)
    for i in range(2, m + 1):
        if a[i] == True:
            for j in range(i + i, n + 1, i):
                a[j] = False
    answer =([i for i in range(2, n + 1) if a[i] == True])
    return answer


n= int(sys.stdin.readline())
for i in range(n):
    k=int(sys.stdin.readline())
    sosulist=(list(combinations(solution(k),2)))
    for i in range(len(sosulist)):
        if sum(sosulist[i])==k:
            print(sosulist[i][0],sosulist[i][1])
            break


n=10000
