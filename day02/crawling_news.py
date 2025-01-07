# crawling_news.py
# 구글 뉴스 사이트에 웹드라이버로 접속하여
# 과학/기술 탭 클릭
# 기사들의 제목과 링크를 추출
# + csv로 내보내기
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 크롬 드라이버초기화
driver = webdriver.Chrome()

# 구글 뉴스 웹페이지 주소
url = "https://news.google.com/home?hl=ko&gl=KR&ceid=KR:ko"

# 해당 웹페이지 주소로 드라이버가 이동
driver.get(url)

# 입력을 받아 다음으로 진행하는 짧은 함수 구현
next = lambda x=None: input("Enter를 입력하여 이어서 진행")
next()

# 클래스 이름이 brSCsc인 태그를 가져와서
result = driver.find_elements(By.CLASS_NAME, "brSCsc")

target = None
# text가 과학/기술인 div를 찾아서
for e in result:
    # 가져온 텍스트를 text 변수에 임시로 담는다.
    text = e.text
    print(text)
    # 해당 텍스트의 내용중 과학이라는 단어가 있다면
    if "과학" in text.strip():
        # 찾고 있던 대상이므로,
        # for문 밖에서 사용하기 위해 target 변수에 담는다.
        target = e
        break
# 
next()

# 클릭해보자.
target.click()

# 페이지가 넘어갔는지 확인해보자.
next()
# 페이지 잘 넘어갔음
# 웹페이지를 확인해보니 gPFEn 클래스를 가진 태그에
# 기사 제목과 해당 기사 페이지로 넘어갈 수 있는
# 링크가 href 속성에 들어있었다.

# gPFEn 클래스를 가진 태그를 모두 들고 온다.
results = driver.find_elements(By.CLASS_NAME, "gPFEn")

# 추출한 데이터를 담을 리스트 선언
datas = list()

# 반복적으로 해당 내용을 추출해온다.
for result in results:
    # result.text가 있는 경우는 기사 제목이 유효했다.
    if result.text:
        # print(result.text)
        href_data = result.get_attribute('href')
        # result.text가 있는 경우에만 기사 제목(text)와
        # 링크(href)를 추출하면 된다.
        # if href_data: print(href_data.split("com")[1][:10])

        # 기사제목(text)과 해당 기사 링크(href)를 튜플로 담는다.
        datas.append((result.text, href_data))
next()

import csv 

file_path = "IT_news.csv"

with open(file_path, 'w', encoding="utf-8-sig", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["기사 제목", "기사 링크"]) # 헤더
    writer.writerows(datas)

print("추출 완료")













