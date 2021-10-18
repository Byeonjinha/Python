from bisect import bisect_left


dataset = [5,10,18,22,35,55,75,103,152]
value = int(input("검색할 숫자:"))
pos = bisect_left(dataset,value)
print('pos :',pos+1)

def BinarySerch(data,target):
    i = bisect_left(dataset,target)
    if dataset[i] == target:
        return i
    else:
        return -1

value = int(input("검색할 숫자 : "))
pos = BinarySerch(dataset,value)
if pos == -1:
    print("찾으실려는 숫자가 없습니다.")
else:
    print("%d는 %번째에 있습니다." % (value,pos))