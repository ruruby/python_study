# -*- coding: utf-8 -*-

import os
import requests
from bs4 import BeautifulSoup

os.mkdir("독립일기")
os.chdir("독립일기")

# 크롤링할 페이지
url="https://comic.naver.com/webtoon/list?titleId=748105&no=124&weekday=sun"
# 크롤링 방지 우회를 위한 헤더 설정
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53'}
content=requests.get(url, headers=headers)
soup=BeautifulSoup(content.content, "html.parser")

# class가 title인 td태그 내용 추출
title=soup.findAll("td",{"class","title"})

for i in title:
    # 회차명으로 디렉토리 생성
    os.mkdir((i.text).strip())
    # 생성한 회차의 디렉토리로 이동
    os.chdir(os.getcwd()+"\\"+(i.text).strip())

    # 각 회차로 이어지는 링크
    url="https://comic.naver.com"+i.a['href']
    # 회차별 내용 크롤링
    each_content=requests.get(url, headers=headers)
    soup=BeautifulSoup(each_content.content, "html.parser")
    # class가 wt_viewer인 div 태그 내의 img태그 내용 추출
    Img=soup.find('div',{"class","wt_viewer"}).findAll("img")
    # 이미지 저장 시 파일 이름
    name=1

    # 하나의 회차 내의 이미지 저장
    for j in Img:
        # 각 이미지의 전체 경로 포함 이름 설정 
        save=os.getcwd()+"\\"+str(name)+".jpg"
        with open(save,"wb") as f:
            src=requests.get(j['src'], headers=headers)
            f.write(src.content)
        # 저장하는 이미지 각각에 다른 이름 부여
        name=name+1
            
    # 상위 디렉토리로 이동
    os.chdir("..")


