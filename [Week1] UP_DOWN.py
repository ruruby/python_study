import random

records=[]
while True:
    print("UP & DOWN 게임에 오신걸 환영합니다~\n1. 게임시작 2. 기록확인 3. 게임종료")
    option=input(">>") #게임 옵션을 사용자로부터 입력받아 변수 option에 저장
    best_record=0
    start=1
    end=100

    if(option=="1"):
        correct_answer=random.randint(start, end) #1이상 100이하 범주의 정수 중 난수 선택하여 정답으로 저장
        for i in range(10):
            guess=int(input("%d번째 숫자 입력(%d~%d) : " %(i+1, start, end)))
            if guess>correct_answer:
                print("DOWN")
                end=guess-1
            elif(guess<correct_answer):
                print("UP")
                start=guess+1
            else:
                print("정답입니다!\n%d번만에 맞추셨습니다" %(i+1))
                records.append(i+1)
                if guess>best_record:
                    best_record=guess
                    print("최고기록 갱신~!")
                break
    elif option=="2":
        for i in range(len(records)):
            print("%d %d" %(i+1, records[i]))
    elif option=="3":
        break
    else:
        print("주어진 옵션에서 선택해주세요.")
            
