# -*- coding: utf-8 -*-

from selenium import webdriver
import time

path="./chromedriver.exe"
driver=webdriver.Chrome(path)

# 게임 사이트 접속
driver.get("http://zzzscore.com/1to50/")


btn=driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')

for i in range(50):
    for e_btn in btn:
        if(e_btn.text==str(i+1)):
            e_btn.click()
            print(e_btn.text+" 클릭")
driver.get("http://zzzscore.com/1to50/#google_vignette")
driver.find_element_by_id('dismiss-button.btn.skip').click()


'''drver.get("http://zzzscore.com/1to50/result")
result=driver.find_element_by_class_name('level')
comment=driver.find_element_by_class_name('comment')
print(result.text)
print(comment.text)'''

driver.close()
