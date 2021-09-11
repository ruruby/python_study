import random

records=[] #기록들을 저장할 list
best_record=0 #최고기록 0으로 초기화

while True:
    print("UP & DOWN 게임에 오신걸 환영합니다~\n1. 게임시작 2. 기록확인 3. 게임종료")
    option=input(">>") #게임 옵션을 사용자로부터 입력받아 변수 option에 저장
    start=1 #사용자가 guessing할 값의 최소값
    end=100 #사용자가 guessing할 값의 최댓값

    if(option=="1"): #1번 옵션을 선택했을 경우
        correct_answer=random.randint(start, end) #1이상 100이하 범주의 정수 중 난수 선택하여 정답으로 저장
        for i in range(10): #게임의 최대 기회는 10번
            guess=int(input("%d번째 숫자 입력(%d~%d) : " %(i+1, start, end))) #사용자가 입력했던 값을 토대로 범위를 알려주며, 사용자의 입력을 새로 받음 
            if guess>correct_answer: #사용자의 입력>정답
                print("DOWN")
                if end>guess: #기존 최댓값보다 현재 입력한 값이 큰 경우에만 사용자가 guessing할 값의 최댓값을 갱신한다.
                    end=guess-1
            elif(guess<correct_answer):#사용자의 입력<정답
                print("UP")
                if start<guess: #기존 최소값보다 현재 입력한 값이 작은 경우에만 사용자가 guessing할 값의 최댓값을 갱신한다.
                    start=guess+1
            else:
                print("정답입니다!\n%d번만에 맞추셨습니다" %(i+1))
                records.append(i+1) #기록을 records리스트에 순서대로 저장
                if i+1>best_record: #최고기록보다 현재의 기록이 좋을 경우 갱신 및 최고기록 갱신 알림
                    best_record=i+1
                    print("최고기록 갱신~!")
                break
    elif option=="2":
        for i in range(len(records)): #기록이 저장된 records리스트의 값을 차례로 출력
            print("%d %d" %(i+1, records[i]))
    elif option=="3":
        break
    else:
        print("주어진 옵션에서 선택해주세요.")
            
