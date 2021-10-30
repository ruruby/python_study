import os.path
# -*- coding: utf-8 -*-

import random
import datetime #날짜 기록을 위한 라이브러리

records=[] #기록들을 저장할 list
best_record=11 #최고기록 11으로 초기화(처음 성공 시에도 최고기록 갱신으로 인정하기 위함)

if os.path.isfile('swing.txt'):
    fr=open('swing.txt', 'r')
    pre=fr.readlines()
    print(pre)
    if len(pre)!=0:
        for i in pre:
            l=i.split()
            records.append(tuple(l))
        best_record=int(records[0][1])

f=open('swing.txt', 'w', encoding="utf8") #최고기록을 기록하기 위한 파일 open

try:
    while True:
        print("UP & DOWN 게임에 오신걸 환영합니다~\n1. 게임시작 2. 기록확인 3. 게임종료")
        option=input(">>") #게임 옵션을 사용자로부터 입력받아 변수 option에 저장
        start=1 #사용자가 guessing할 값의 최소값
        end=100 #사용자가 guessing할 값의 최댓값
        
        if(option=="1"): #1번 옵션을 선택했을 경우
            correct_answer=random.randint(start, end) #1이상 100이하 범주의 정수 중 난수 선택하여 정답으로 저장
            for i in range(10): #게임의 최대 기회는 10번
                guess=int(input("%d번째 숫자 입력(%d~%d) : " %(i+1, start, end))) #사용자가 입력했던 값을 토대로 범위를 알려주며, 사용자의 입력을 새로 받음
                while guess<0 or 100<guess: #피드백 1번 반영
                    print("범주 외의 숫자를 입력하셨습니다. 1이상 100이하의 숫자를 입력하십시오.")
                    guess=int(input("%d번째 숫자 입력(%d~%d) : " %(i+1, start, end)))
            
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
                    #records.append(i+1) #기록을 records리스트에 순서대로 저장
                    if i+1<best_record: #최고기록보다 현재의 기록이 좋을 경우 갱신 및 최고기록 갱신 알림 #피드백 3번 반영
                        dt_best = datetime.datetime.now() #최고기록 순간의 시간 기록
                        dt_best=dt_best.strftime('%Y-%m-%d')
                        best_record=i+1
                        print("최고기록 갱신~!")
                        nickname=input("닉네임을 입력해주십시오>>")
                        records.append((nickname, best_record, dt_best)) 
                    break
                    
        elif option=="2":
            records.sort(key=lambda x:x[1]) #피드백 2번 반영(최고기록 순으로 정렬)
            for i in range(len(records)): #기록이 저장된 records리스트의 값을 차례로 출력
                print(str(i+1)+ " " +records[i][0]+ " "  + str(records[i][1])+ " ", end="")
                print(records[i][2])
        elif option=="3":
            records.sort(key=lambda x:x[1])
            for i in range(len(records)): #기록이 저장된 records리스트의 값을 txt 파일에 저장
                f.write(records[i][0]+ " " + str(records[i][1])+" ")
                f.write(records[i][2])
            break
        else:
            print("주어진 옵션에서 선택해주세요.")
except:
    print("에러가 발생하여 게임이 종료되었습니다.")

f.close()

