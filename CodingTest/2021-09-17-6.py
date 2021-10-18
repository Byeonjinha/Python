import sys
def dduckgilee(M,dduck):
    start =0                 # 시작점
    result = 0               # 결과 값
    end = max(dduck)         # 가장 긴 떡 길이의 점
    while(start <= end):     # 가장 긴 떡의 길이가 시작점 보다 작을 때 까지 반복
        total = 0            # 총길이 정의
        mid = (start+end)//2     #  mid 지점은 시작 점 + 가장 긴 떡길이의 점을 2로 나눠 절삭 한 값이 됨
        for x in range(len(dduck)):          # 주어진 떡들을 순차적으로 돌림
             if dduck[x]>mid:                # x번째 떡의 길이가 mid 값보다 작다면
                total += dduck[x] -mid       #   총길이 += x번째 떡의 길이 -mid 값
        if total < M:                        # 만약 총길이 보다 요청한 떡 길이가 작다면
            end = mid -1                     # 가장 떡의 점은 가운데 점 -1
        else :                               # 만약 총길이 보다 요청한 떡 길이가 작지않다면 ( 같거나 크다면 )
            result = mid                     #  결과는 가운데 점이 됨
            start = mid +1                   # 시작은 가운데 점 +1 이 됨
    return result                            # result 값 리턴

N,M = list(map(int,sys.stdin.readline().split()))       # 입력 받은 N, M 정의
dduck = list(map(int,sys.stdin.readline().split()))     # 떡 list 입력받음
answer =dduckgilee(M,dduck)                             # answer 을 메소드 실행리턴 값으로 정의
print(answer)                                           # answer return