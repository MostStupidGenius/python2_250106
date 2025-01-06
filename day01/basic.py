# 변수 : 값을 담기 위한 저장공간(하나의 값만 담을 수 있다.)
# 자료형
    # 숫자형, 문자형, 논리형
# 연산자
    # 수 수 수
    # 수 수 논
    # 논 논 논
# 이터러블 객체(iterable)
# 리스트 [] : "변경O, 순서O(인덱스), 중복O"
# 튜플 () : "변경불가"
# 세트 {} : 변경가능, 순서X(특정 값), "중복X"
# 딕셔너리 {k:v} : 마치 변수처럼 "키값과 value값"으로 나뉘어있다.
# 제어문
    # if문 : 조건식에 따라서 건너뛰거나 해당 코드를 실행
        # elif : 여러 조건을 준다.
        # else : 위의 조건식이 모두 거짓인 경우
    # while문 : 조건식이 만족하는 동안 코드 무한반복 실행
    # for문 : 이터러블 객체의 요소를 하나씩 들고 와서 반복
        # range(10) 0~9까지의 등차수열을 만든다.
        # enumerate(iter)
            # 인덱스와 요소를 튜플로 담아서 반환
        # 진행도 progress bar
            # tqdm
# 함수
    # 수업예정 *args, **kwargs
    # 매개 변수 기본값 설정
    # 타입힌트
def func(name: str="이름없음") -> None:
    print(name)
    # return name
# func(name="이준상")
func()
    # map, filter, reduce
    # 리스트 컴프리헨션
    # 
    # 튜플 컴프리헨션
# 클래스
# 클래스 self
# 상속
    # super
# 매직 메서드
