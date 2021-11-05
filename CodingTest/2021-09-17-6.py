import sys
def dfs(dduck, v, gilee):

    global sum, M


    gilee[v] = True
    for i in range(len(dduck)):
       if dduck[i]+v-(max(dduck)) >= 0 :
        sum+=1

        if sum >= M:
            print(sum, M)
            return (sum,v)

    for i in range(len(gilee)):
        if not gilee[i]:
            dfs(dduck, i , gilee)

N,M = list(map(int,sys.stdin.readline().split()))       # 입력 받은 N, M 정의
dduck = list(map(int,sys.stdin.readline().split()))
sum = 0
gilee = [False]*M
a = dfs(dduck,0,gilee)
print(a, end='d')