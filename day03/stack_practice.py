# 스택을 파이썬 클래스로 구현
class My_stack(list):
    def __init__(self):
        # 내부적으로 My_stack 객체를 리스트다.
        super().__init__()
    
    # 데이터 추가
    def push(self, data):
        self.append(data)
    
    # 데이터 제거
    def pop(self):
        # 무조건 마지막 요소를 반환하도록 제어
        return super().pop(-1)
    
    # 중간에 삽입하는 insert 기능에서 인덱스를 넣을 수 없게 하여
    # 무조건 push 메서드로 통하게끔 설정
    def insert(self, data):
        self.push(data)
    
    # def extend(self, iterable):
    #     return super().extend(iterable)

if __name__ == "__main__":
    s = My_stack()
    for i in range(5):
        s.push(i)
        s.insert(i*2)
        s.append(i*3)
    
    print(s)
    print("================")
    
    for i in range(5):
        print(s.pop())
        print(s)