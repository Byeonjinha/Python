def solution(strings, n):
    strings2=[]
    answer=[]
    j=""
    for i in strings:
        i = list(i)
        strings2.append(i)
        print(strings2)
    sorted(strings2, key=lambda x: x[0])

    for i in strings2:
        j= "".join(i)
        answer.append(j)
    print(answer)
    return answer


strings = ["abce", "abcd", "cdx"]
n =1


solution(strings, n)