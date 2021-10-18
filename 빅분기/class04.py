# 1-03. 이름(변수), 타입(type)


# [1] 10 이라는 정수 객체에 'a'라는 이름을 붙여 저장하고,
# print 함수를 사용해 class와 객체를 출력한다
# type(a)는 a라는 객체의 class를 출력하는 함수이다
a=10
print(type(a),a)

# [2] 3.14 라는 float 객체에 'a' 라는 이름을 붙여 저장하고,
# print 함수를 사용해 class와 객체를 출력한다
a=3.14
print(type(a),a)

# [3] True 라는 bool 객체에 'a'라는 이름을 붙여 저장하고,
# print 함수를 사용ㅇ해 class와 객체를 출력한다
a= True
print(type(a),a)

print(True+True , True*False) # True: 1, False:0
# [4] 'python' 이라는 str 객체에 'a' 라는 이름을 붙여 저장하고,
# print 함수를 사용해 class와 객체를 출력한다
a= 'python'
print(type(a),a)
a=(1)
b=(1,)
c=(1,2)
print(type(a),type(b),type(c))
# [5] 여러 개의 객체를묶어 놓은 객체를 Container라고 하며
# 묶음 기호에 따라 여러 종류의 Container가 있음
# tuple : (1,)
# list  : [1]
# set   : {1}
# dict  : {'one':1} -> {'apple':'사과', key:value}
a = (1,2,3)
b = [1,2,3,]
c = {'A':65, 'B':66, 'C':67}
print(type(a),a)
print(type(b),b)
print(type(c),c)

# [6] 아래의 10에 대해서 a라는 이름을 사용하여 변경하면 좋아지는 것은 무엇인가?
print(type(10), id(1), dir(10), sep="\n")
a=3.5
print(type(a), id(a),dir(a), sep='\n  ')
# total
# avg
# weight,height
# 영문, 숫자, _(under score), 한글(비권장)
# 숫자는 첫 번째 글자로 사용하지 않음 (사용시 Error)
# _ : 첫 번째 글자로 사용할 수 있지만 하지 않는 것을 권유
# keyword : 의미있는 단어
# - 이름을 사용하지 못함 (사용시 Error)
# if = 100
ab1= 10