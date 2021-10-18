import  random
import sys                 # 라이브러리 참조

start='1'

while start !='2':    # start 가 '2'이면 게임종료
    step1 = '1'
    answer = random.randrange(100, 1000)  # 랜덤생성
    while step1 != '2':
        step2='1'
        answer_list = list(str(answer))  # 비교하기 위해 리스트화

        while step2 != '2':
            print("100~999 사이의 값을 입력해주세요.", end="  ")
            step3='0'
            step4='0'
            strike = 0
            ball = 0

            input1= sys.stdin.readline().strip()
            input_list = list(input1)
            if 100<=int(input1)<1000:
                step1= '2'
            else:
                print("100~999 사이의 값을 입력해주세요.")
            for i in range(len(input_list)):                          #비교
                for j in range(len(answer_list)):
                    if input_list[i] == answer_list[j] and i==j:
                        strike +=1
                    elif input_list[i] == answer_list[j] and i!=j:
                        ball +=1

            print("스트라이크",strike,"볼",ball)


            if answer_list==input_list:
                while step4 != '2':
                    print("게임을 새로 시작하려면 1, 종료하려면 2를 입력하세요.")
                    start= sys.stdin.readline().strip()
                    if start=='1'or start =='2':
                        step2='2'
                        step4='2'
                    else:
                        print('1과 2 중 하나만 입력부탁드려요.')