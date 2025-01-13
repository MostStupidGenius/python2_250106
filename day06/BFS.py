# BFS.py
# 너비 우선 탐색(Breadth-First Search)
# Queue를 사용하여 구현
# 시작 정점으로부터 가까운 정점을 먼저 방문하고
# 멀리 떨어져 있는 정점을 나중에 방문

# BFS 구현(리스트 활용 Queue)
def bfs(graph: dict, start):
    # 방문한 정점을 저장할 set 자료구조 초기화
    visited = set()
    # 시작 정점을 포함한 queue 생성
    queue = [start]
    # 시작 정점을 방문 처리
    visited.add(start)

    # queue가 빌 때까지 반복
    while queue:
        # 큐에서 가장 왼쪽 정점을 꺼냄(선입선출)
        vertex = queue.pop(0)

        # 현재 방문 중인 정점 출력(공백으로 구분)
        print(vertex, end=" ")

        # 현재 정점의 이웃 정점들을 순회
        for neighbor in graph[vertex]:
            # 아직 방문하지 않은 정점에 대해
            if neighbor not in visited:
                # 방문 처리
                visited.add(neighbor)
                # 큐에 오른쪽에 이웃 정점 추가
                queue.append(neighbor)

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
    bfs(graph, start)