# start.py
# pip install requests beautifulsoup4 selenium
# requests 라이브러리로 웹페이지 문서 받아오기
import requests

def request_naver():
    # 웹페이지 주소 설정
    url = "https://www.naver.com"

    # 웹페이지 요청에 대한 응답
    response = requests.get(url)

    # 응답의 텍스트를 추출
    print(response.text)

# 단순 텍스트로 가져오는 건, 데이터를 추출하기 어렵다
# 그래서 가져온 웹페이지 텍스트를 파이썬에서 다루기 쉽게
# 바꿔주는 bs4 라이브러리로 parsing을 해야 한다.
from bs4 import BeautifulSoup as Bs

url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/#"

response = requests.get(url)

# 가져온 response의 text를 bs4를 이용해서 파싱
soup = Bs(response.text, 'html.parser')

def get_divs():
    # 태그 중 가장 자주 쓰이는 div태그를 모두 추출하기
    divs = soup.find_all('div')
    # 각각의 div 태그의 클래스
    for div in divs:
        # 클래스 속성 추출
        result = div.get('class')
        # result값이 비어있지 않다면(찾았다면) 출력
        if result is not None: print(result)
# get_divs()





