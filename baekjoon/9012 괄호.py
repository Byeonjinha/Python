import sys
count=int(0)
def gwalho(T):
    for i in range(T):
        gwal= list(sys.stdin.readline())
        gwal.pop(-1)
        if len(gwal)%2!=0:      #짝수아니면 NO
            print("NO")         #
            continue
        if gwal[0]==")":        # )로시작하면 NO
            print("NO")         #
            continue
        else:
            gumsa(gwal)
def gumsa(gwal):
    global count
    count = 0      # count 초기화
    for i in range(len(gwal)):      #)가 (보다 앞에나오면 No
        if gwal[i]=="(":            #
            count=count+1           #
        elif gwal[i]==")":          #
            count=count-1           #
            if count<0:             #
                print("NO")         #
                break
    if count==0:
        print("YES")    #() 짝의 개수가 맞으면 Yes
    elif count>0:       # () 가 0을 넘으면 No
        print("N0")
    return

T = int(sys.stdin.readline())
gwalho(T)