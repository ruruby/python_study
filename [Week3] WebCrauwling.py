# -*- coding: euc-kr -*-

from bs4 import BeautifulSoup
import urllib.request

web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')
print("*** ���￩�ڴ��б� �а� �� Ȩ������ ���� ***\n\t�а�\t\tȨ������")

#a�±װ� ������ ���� ����
site=soup.findAll('a')

for a in site:
    # ��¿� �������� ���� �������, ���������к�, ���� ���п� ����
    if a.text=="�������" or a.text=="���������к�" or "���п�" in a.text:
         #or a.text.encode('utf-8').contains("���п�")
        continue
    # ����� ���� �а� �� ������ ���, href���� �����۸�ũ�� �ɷ��ִ� �ش� �������� �̵��Ͽ� ũ�Ѹ� 
    else:
        href=a.attrs['href']
        page=urllib.request.urlopen('http://www.swu.ac.kr'+href)
        bsoup=BeautifulSoup(page, 'html.parser')
        t=bsoup.findAll('a', 'btn btn_xl btn_blue_gray')        

        # Ȩ������ �ٷΰ��� ���簡 ù��°�� �����ϴ� �� ���η� Ȩ������ ���翩�� Ȯ��
        # (�ڵ� �ۼ��ڰ� Ȩ������ �ٷΰ��Ⱑ ��� �̸� �ּ�ó���Ͽ� �ڵ带 ���ܳ��ұ� ������, ���翩�θ����� �Ǵ��ϱ�  �����Ͽ� ������ ���)
        for j in t:
            if "Ȩ������ �ٷΰ���"==j.text or "Ȩ�������ٷΰ���"==j.text:
                print(a.text + "\t\t" + j.attrs['href'])
                break
            else:
                print(a.text + "\t\t" + "Ȩ�������� �������� ����")
                break

