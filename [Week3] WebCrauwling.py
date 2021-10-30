# -*- coding: euc-kr -*-

from bs4 import BeautifulSoup
import urllib.request

web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')
print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n\t학과\t\t홈페이지")

#a태그가 포함한 내용 추출
site=soup.findAll('a')

for a in site:
    # 출력에 포함하지 않을 교양대학, 자율전공학부, 각종 대학원 제외
    if a.text=="교양대학" or a.text=="자율전공학부" or "대학원" in a.text:
         #or a.text.encode('utf-8').contains("대학원")
        continue
    # 출력을 위한 학과 및 전공의 경우, href으로 하이퍼링크가 걸려있는 해당 페이지로 이동하여 크롤링 
    else:
        href=a.attrs['href']
        page=urllib.request.urlopen('http://www.swu.ac.kr'+href)
        bsoup=BeautifulSoup(page, 'html.parser')
        t=bsoup.findAll('a', 'btn btn_xl btn_blue_gray')        

        # 홈페이지 바로가기 존재가 첫번째로 등장하는 지 여부로 홈페이지 존재여부 확인
        # (코드 작성자가 홈페이지 바로가기가 없어도 이를 주석처리하여 코드를 남겨놓았기 때문에, 존재여부만으로 판단하긴  부족하여 선택한 방법)
        for j in t:
            if "홈페이지 바로가기"==j.text or "홈페이지바로가기"==j.text:
                print(a.text + "\t\t" + j.attrs['href'])
                break
            else:
                print(a.text + "\t\t" + "홈페이지가 존재하지 않음")
                break

