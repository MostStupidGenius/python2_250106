# regular_expression.py
# 정규 표현식
# 문자열의 특정한 패턴을 정규 표현식으로 표현하여
# 그러한 패턴을 찾아내거나 일치여부 판단,
# 해당 패턴의 문자열을 다른 문자열로 대체,
# 추출, 그룹화, 검색, 유효성 검사 등에 쓰인다.
# 예시) 아이디, 비밀번호, 이메일 유효성 검사

# re 모듈을 임포트 해야 한다.
import re

# + 1번 이상 반복


text = "123a45b c6d7"
# 여러 숫자가 연속된 것들만 모아보기
pattern1 = re.compile(r"\d+") # 숫자가 하나 이상인 덩어리

# \w 모든 문자를 가리킨다.
pattern1 = re.compile(r"\w+") # ['123a45b', 'c6d7']

# 문자열 클래스[]
# 대괄호[] 안에 들어가는 규칙에 따른 문자열 값을
# 선별한다.
pattern1 = re.compile(r"[a-c1-4]+")

# 문자열의 시작 ^
# 문자열의 끝 $
pattern1 = re.compile(r"^\d+") # ['123']

matches = pattern1.findall(text)
print(matches) # ['123', '45', '6', '7']