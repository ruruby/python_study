# -*- coding: utf-8 -*-

from selenium import webdriver
import time

path="./chromedriver.exe"
driver=webdriver.Chrome(path)

# 게임 사이트 접속
driver.get("http://zzzscore.com/1to50/")

# 숫자 버튼에 해당하는 요소의 XPath 값 지정하여 숫자버튼들 모두 가져옴
btn=driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

# 버튼에 쓰여진 text가 1부터 50까지의 숫자인지 확인하기 위해 반복 
for i in range(50):
    for e_btn in btn: # 앞서 가져온 숫자 버튼들 중 현재 클릭해야하는 숫자에 해당하는 버튼이 어떤 것인지 확인하기 위한 반복
        if(e_btn.text==str(i+1)):
            e_btn.click()
            print(e_btn.text+" 클릭")
            
# 게임 완료 후, 결과 창 보기 전에 뜨는 광고창의 x를 클릭해서 닫기
driver.get("http://zzzscore.com/1to50/#google_vignette")
driver.find_element_by_id('dismiss-button.btn.skip').click()

# 결과를 가져와서 출력해주고 싶었으나 실패
'''drver.get("http://zzzscore.com/1to50/result")
result=driver.find_element_by_class_name('level')
comment=driver.find_element_by_class_name('comment')
print(result.text)
print(comment.text)'''

driver.close()
