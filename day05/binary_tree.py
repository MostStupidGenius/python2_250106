# binary_tree.py
# 이진 트리
# 노드를 기준으로 왼쪽과 오른쪽 최대 두 개의 자식 노드를 가지는
# 노드들로 트리 구조를 이루는 것을 말한다.
# 이러한 이진트리를 만드는 기본 개념은
# 연결 리스트의 연장선에 있다.

# 노드는 노드 자체의 데이터와 자식 노드의 주소를 가지는
# left, right로 구성된다.
class Node():
    def __init__(self, data):
        # 노드의 데이터를 저장
        self.data = data
        # 노드의 자식 노드 주소를 저장할 변수
        self.left: Node = None
        self.right: Node = None
    
    def __str__(self):
        str = f"data: {self.data}\
        \n\tleft: {self.left.data if self.left else ''}\
        \n\tright: {self.right.data if self.right else ''}"
        # print(f"data: {self.data}")
        # print(f"\tleft: {self.left.data if self.left else ''}")
        # print(f"\tright: {self.right.data if self.right else ''}")
        return str

# 이진 트리는 루트 노드(최상위 노드)에 해당하는 root와
# 그 루트에서 연결된 다른 노드들로 이루어진다.
class Binary_tree():
    def __init__(self):
        # 루트 노드를 저장할 변수
        self.root: Node = None
    
    # 데이터 삽입
    # 루트가 있다면 루트 노드를 queue에 담는다.
    # queue에 담긴 노드를 순차적으로 꺼내서,
    # left와 right를 확인한다
    # 1. None인 경우, 해당 포인터에 새로운 노드를 추가한다.
    # 2. None이 아닌 경우, queue에 추가한다.
    # 새로운 노드가 추가되지 않았다면 queue에서 노드를 꺼내서 반복한다.
    def insert(self, data): # 새로운 데이터를 트리에 추가
        # 새로운 데이터를 노드로 만든다
        new_node = Node(data)

        # 만약 루트 노드가 없다면
        if not self.root:
            # 새로운 데이터를 노드를 만들어서 삽입한다.
            self.root = new_node
            return

        # 만약 루트 노드가 있다면 루트를 queue에 담는다.
        # 여기서는 queue를 리스트를 이용해서 pop(0)으로
        # queue를 간이 구현할 것이다.
        queue = [self.root]

        # queue가 비어있지 않다면 무한 반복하여 순회
        while(queue):
            # queue에서 새로운 노드를 꺼낸다
            node = queue.pop(0)
            # 이 노드에 대해서 왼쪽 자식과 오른쪽 자식을 검사한다.
            # 왼쪽 노드가 없다면
            if not node.left:
                # 왼쪽 노드에 새로운 노드를 만들어서 삽입
                node.left = new_node
                # 메서드 종료
                return
            elif not node.right:
                node.right = new_node
                return
            # 만약 자식 노드 모두가 비어있지 않다면
            # 해당 자식 노드들을 모두 queue에 담는다.
            queue.append(node.left)
            queue.append(node.right)

    # 이진트리 순회


if __name__ == "__main__":
    bt = Binary_tree()
    bt.insert(3)
    bt.insert("홍길동")
    bt.insert("홍길동2")
    bt.insert("홍길동3")
    bt.insert("홍길동4")
    print(bt.root)

