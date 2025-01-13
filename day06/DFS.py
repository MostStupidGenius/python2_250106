# DFS.py
# 깊이 우선 탐색(Depth-First Search)
# 깊은 부분을 먼저 탐색하는 알고리즘
# 왔던 길이 아닌 가던 방향으로 더 이상 연결된 간선이 없다면
# 이전 갈림길로 돌아가 다른 간선을 확인한다.
# 다른 간선이 없으면 그 이전 갈림길로 돌아간다.

# 재귀를 사용한 DFS 구현
def dfs_recursive(graph:dict, start, visited:set=set()):
    """
    graph: dict 자료형으로 작성된, 인접 리스트 그래프가 표현된 값이다.
    start: 현재 노드(정점)를 전달 받는다. graph의 키값과 동일해야 한다.
    visited: 방문한 노드(정점)를 set 자료형에 담아
        방문했는지 여부를 확인하는 용도로 쓰인다.
    """
    # visited가 None이면 최초 호출이므로, 새로운 set 생성
    # if visited is None:
    #     visited = set()
    # -> 매개변수의 기본값으로 set()을 설정
    
    # 현재 정점을 방문 처리
    visited.add(start)
    print(start, end=" ") # 방문한 노드 출력

    # 현재 정점의 이웃 정점들을 탐색
    for next_node in graph[start]:
        # 아직 방문하지 않은 이웃 정점에 대해 재귀적으로 DFS 수행
        if next_node not in visited:
            dfs_recursive(graph, next_node, visited)

# 스택을 이용한 DFS 구현
def dfs_iterative(graph:dict, start):
    # 방문 여부를 담을 변수 선언
    visited = set()
    # 스택에 이용할 리스트 선언 및 start 대입하여 초기화
    stack = [start]

    # stack이 남아 있다면 무한 반복
    while stack:
        # 스택에서 정점을 꺼냄(가장 최근 추가된 노드)
        vertex = stack.pop(-1)

        # 아직 방문하지 않은 정점이라면
        if vertex not in visited:
            # 방문 처리
            visited.add(vertex)
            # 노드 출력
            print(vertex, end=" ")

            # 현재 정점의 이웃 정점들을 스택에 추가
            # (방문하지 않은 정점만 추가한다.)
            # 리스트 컴프리헨션으로 리스트가 만들어지므로
            # 요소 하나하나를 stack에 추가하려면
            # .extend()로 추가해야 한다.
            stack.extend([e for e in graph[vertex] if e not in visited])

if __name__ == "__main__":
    graph = {
        'A' : ['B', 'C'],
        'B' : ['A', 'D', 'E'],
        'C' : ['A', 'F'],
        'D' : ['B'],
        'E' : ['B', 'F'],
        'F' : ['C', 'E']
    }
    start = 'A'
    dfs_recursive(graph, start)
    print("")
    dfs_iterative(graph, start)












