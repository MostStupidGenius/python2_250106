# linked_list.py
# 연결 리스트
# 노드와 노드를 연결하여 다음 노드로 이동하는 속도가
# 빠른 자료구조이다.
# 각 노드는 다음 노드를 가리키는 주소값(포인터)과
# 해당 노드의 데이터를 담고 있다.

# 노드 클래스를 먼저 정의하고
# 이를 다루기 위한 링크드 리스트 클래스를 만들어야 한다.

# 노드 클래스
class Node():
    def __init__(self, data):
        self.data = data
        self.next: Node = None

    def set_next_Node(self, next_node):
        self.next = next_node
        return self

# 연결 리스트 클래스
class Linked_list():
    def __init__(self, head:Node=None):
        # 연결 리스트의 첫번째 노드를 head라고 부른다.
        self.head = head

    # 노드 삽입
    # 새로운 노드를 링크드 리스트에 추가합니다.
    def insert(self, node: Node):
        # 새로운 노드의 주소를 담을 마지막 노드를 찾아야 한다.
        last_node = None
        # head가 있는지 먼저 검사
        if self.head:
            last_node = self.head
        else:
            # 만약 헤드가 없다면
            # 새로운 노드를 헤드로 설정
            self.head = node
            # 여기서 return을 하는 이유는
            # 아래의 마지막 노드를 찾는 동작을
            # 하지 않고 메서드를 조기 종료하기 위해서이다.
            return self
        
        # 마지막 노드의 next가 없을 때까지
        # -> 마지막 노드를 링크드 리스트에서 찾을 때까지 반복
        while(last_node.next):
            last_node = last_node.next
        # 마지막 노드의 next가 없다면
        last_node.next = node
        if self.find(node.next): node.next = None
        return self

    # 노드를 찾아서 반환하는 메서드
    def find(self, target: Node):
        # target 노드를 next로 가지는 노드를 찾는다
        current_node = self.head
        while(current_node):
            # 현재 노드의 next와 전달받은 노드를 비교한다.
            if current_node.next == target:
                break
            else:
                current_node = current_node.next
        # 만약 current_node가 None이라면
        # 찾고자 하는 node를 찾지 못한 것이다.
        # if current_node is None: return None
        # current_node에는 찾고자 하는 노드를 찾았다면
        # node가 들어있을 것이고
        # 찾지 못했다면 None이 들어가 있을 것이다.
        # 그렇기 때문에 current_node만 반환해도 된다.
        return current_node # 일괄처리

    # 노드 삭제
    # 특정 노드를 링크드 리스트에서 삭제합니다.
    # target 노드를 전달받아 target 노드를 가리키는
    # 직전의 노드를 찾는다.
    # 직전의 노드가 가리키는 주소를 target 노드가 가리키는
    # 주소로 바꾼다. -> taget 노드를 가리키는 노드가 없어진다
    def delete(self, node: Node) -> Node:
        # # target 노드를 next로 가지는 노드를 찾는다
        # current_node = self.head
        # while(current_node):
        #     # 현재 노드의 next와 전달받은 노드를 비교한다.
        #     if current_node.next == node:
        #         break
        #     else:
        #         current_node = current_node.next
        # # 만약 current_node가 None이라면
        # # 지우고자 하는 node를 찾지 못한 것이다.
        # if current_node is None: return None

        # 찾고자 하는 노드를 찾는 find메서드를 호출하는 것으로
        # "찾는 코드"를 줄일 수 있다.
        current_node = self.find(target=node)

        # current_node의 next가 전달받은 node와 같다면
        # current_node의 next를 전달받은 node의 next로 바꾼다.
        current_node.next = node.next
        # 정상적으로 해당 노드를 제거했다면
        # 제거한 노드를 반환한다.
        return node

    # 노드 탐색
    # 특정 데이터를 가진 노드를 찾습니다.
    # 다음 노드를 반복적으로 확인하여
    # node.data와 전달받은 data가 같은지 확인한다.
    # 만약 같다면, 해당 node를 반환한다.
    def search(self, data):
        # 일단 헤드를 현재 노드로 넣는다.
        current_node = self.head
        # 현재 노드가 있다면
        while(current_node):
            # 현재 노드의 데이터가 전달받은 데이터와 같다면
            if current_node.data == data or current_node.data is data:
                # 현재 노드를 반환
                return current_node
            current_node = current_node.next

        # 1. 헤드가 없는 경우
        # 2. 노드를 전부 순회(current_node==None)했지만
        #    찾으려는 데이터를 찾지 못한 경우
        return None 


    # 순회
    # 모든 노드를 방문하여 데이터들을 리스트에 담아서 반환
    def traversal(self) -> list:
        # 반환할 리스트를 초기화
        result = list()
        # 일단 헤드를 currernt에 담는다.
        current = self.head
        # 현재 current가 None이 아니라면 반복
        while(current):
            # result에 현재 노드의 data를 추가한다.
            result.append(current.data)
            # 현재 노드의 다음 노드를 current에 담는다.
            current = current.next
        # 마지막으로 담긴 current가 None이면 
        # while문을 탈출하여 result를 반환한다.
        return result

    # print()를 하면 전체 데이터가 담긴 리스트를 반환
    def __str__(self):
        return str(self.traversal())
    
if __name__ == "__main__":
    link = Linked_list()
    # 나중에 찾거나 지우기 위해 따로 빼놓은 노드
    target_node = Node(6)

    # 체이닝 기법
    # cascading method
    # 메서드 내에서 return을 self로 하여
    # 주소값을 반환, 객체를 반환한 것이기 때문에
    # 해당 객체의 속성, 기능(메서드)에 이어서 접근이 가능하다.
    link.insert(Node(1))\
        .insert(Node(2))\
        .insert(Node(3))\
        .insert(target_node)\
        .insert(Node(4))\
        .insert(Node(5))
    
    # 현재 링크드 리스트 확인
    print("current:\n", link)

    # 타겟 노드를 찾아서 삭제
    link.delete(target_node)
    print("\ndeleted:\n", link)

    # 타겟 노드를 마지막에 추가
    link.insert(target_node)
    print("\ninserted:\n", link)

    # 전체 데이터 순회한 리스트 반환
    print("\nall: ", link.traversal())
