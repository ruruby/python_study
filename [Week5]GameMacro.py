from selenium import webdriver
import time

path="./chromedriver.exe"
driver=webdriver.Chrome(path)

# 게임 사이트에 접속
driver.get("http://zzzscore.com/1to50/")

btn=driver.find_element_by_xpath('//*[@id="grid"]/div[4]')
btn.click()

//*[@id="grid"]/div[6]#5일때
//*[@id="grid"]/div[9] #15일때
//*[@id="grid"]/div[7]#8일때
