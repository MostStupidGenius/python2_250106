# selenium_pratice.py
# 셀레니움으로 동적인 웹페이지 요청
# JS로 동적으로 생성되는 콘텐츠를 크롤링(정보수집)하기 위해
# selenium이라는 라이브러리를 사용한다.
# 방식: webdriver라는 웹 브라우저를 코드로 제어할 수 있는
# 프로그램을 이용하는 것이다.
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Chrome WebDriver 초기화
# 적절한 웹드라이버를 자동으로 설정
driver = webdriver.Chrome()
# url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/#"
url = "https://www.selenium.dev/documentation/"
# 웹드라이버에 해당 웹페이지 주소를 요청
driver.get(url)
# input("종료하려면 엔터")
def presence_element():
    # 특정 요소가 로드 될 때까지 대기
    element = WebDriverWait(driver, 10).until(
        # 특정 요소를 지정하는 부분
        EC.presence_of_element_located((By.CLASS_NAME, "text-end"))
    )
    # 로드가 되어 가져온 해당 요소의 텍스트 출력
    print("", element.text, "")
# presence_element()

target = (By.CLASS_NAME, "nav-item")

result = driver.find_elements(target[0], target[1])
for e in result:
    print(e.text)