# 1-01. 객체(Object)
# 실 세계에 있는 모든 개념을 컴퓨터 세계에 반영하여 저장한것
# 객체는 type과 type이 아닌 것으로 나뉨
# type 인 것 (class) : int,float,bool,str,list,tupe,set,dict, function,module 같은 것이 있음
# type이 아닌 것(instance): 실제 연산할 값6을 갖는 10, 3.14, True ,'python' 등이 있음


# [1] class(=type) , instance
print(int,10)
# [2] 연산자, 함수, (점근 연산자) 사용
10 +20 , abs(-10), (10).__abs__(), (10).__add__(20)

print('python'.upper())

# [3] 객체의 type, 주소, 자주 사용되는 기능 목록 확인
print(type(10), id(int), dir(10))


