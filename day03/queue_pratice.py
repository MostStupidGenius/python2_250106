# queue 자료구조
# 먼저 들어온 데이터가 먼저 나가는
# 대기열과 같은 자료구조이다.
# FIFO first in first out
# 스케쥴러, 절차적인 자동화 작업

def col_deque():
    # collections의 .deque를 사용한 Queue구현
    from collections import deque

    queue = deque()
    queue.append(1) # 요소 추가
    queue.append(2) # 요소 추가
    queue.append(3) # 요소 추가
    queue.append(1) # 요소 추가
    queue.append(5) # 요소 추가

    # 현재 요소 출력
    print(queue)

    print(queue.popleft()) # 첫번째 요소 제거: 1
    print(queue) # 남은 요소 출력
    print(queue.popleft()) # 두번째 요소 제거: 2
    print(queue) # 남은 요소 출력
    print(queue.popleft()) # 세번째 요소 제거: 3
    print(queue) # 남은 요소 출력

def queue():
    # queue.Queue를 사용한 Queue 구현
    # 멀티 스레드 환경에서 안전하게 사용할 수 있도록
    # 설계된 Queue 라이브러리이다.
    from queue import Queue

    queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    queue.put(4)
    queue.put(5)

    # 요소 제거 및 출력
    print(queue.get()) # 첫번째 요소 1 제거
    print(queue.get()) # 요소 2 제거
    print(queue.get()) # 요소 3 제거
    print(queue.get()) # 요소 4 제거

class My_queue():
    def __init__(self):
        # 내부적으로 리스트를 사용한다.
        self.queue = list()
    
    # 데이터를 추가하는 메서드
    def enqueue(self, data) -> bool:
        try:
            # 데이터를 리스트에 추가한다.
            self.queue.append(data)
        except Exception as e:
            # 오류가 생겼다면 False 반환
            print(e)
            return False
        # 오류가 없다면 True 반환
        return True
    
    # queue에서 순서에 따라 데이터를 제거하고 반환
    def dequeue(self):
        try:
            return self.queue.pop(0)
        except Exception as e:
            # 오류가 있다면 None 반환
            return None
        
    def __str__(self):
        # result = f'Queue [{", ".join(list(map(lambda x:str(x), self.queue)))}]'
        # self.queue에 담긴 값이 문자열이 아닐 수 있으니
        # 문자열로 모두 바꿔준다.
        str_queue = [str(e) for e in self.queue]
        
        # 바뀐 문자열 리스트를 ", "를 각 요소들 사이에 삽입하여
        # 하나의 문자열로 합쳐준다.
        joined_queue = ", ".join(str_queue)

        # 그 값을 f스트링으로 이쁘게 뽑아준다.
        result = f"Queue [{joined_queue}]"
        return result

if __name__ == "__main__":
    q = My_queue()
    for i in range(10):
        q.enqueue(i)
    
    print(q)
    for i in range(5):
        print("deque: ", q.dequeue())
        print("current: ", q)
        print()











