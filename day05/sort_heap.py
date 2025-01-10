# sort_heap.py
# 힙 정렬
# 힙(heap)이란, 완전 이진 트리로 만들어진 구조로,
# 루트 노드는 가장 큰 값이 위치하며,
# 부모노드는 자식노드보다 크거나 같은 값이 위치하는 형태를 가진다.

# 최대 힙 속성 유지를 위한 heapify
def heapify(arr, n, i):
    """
    arr: 전체 배열
    n: 힙 크기
    i: 현재 노드의 인덱스
    """
    # 현재 노드를 largest로 초기화
    largest = i

    # 왼쪽 자식 노드의 인덱스 계산(2i + 1)
    left = 2 * i + 1
    # 오른쪽 자식 노드의 인덱스 계산(2i + 2)
    right = 2 * i + 2

    # 왼쪽 자식이 힙 크기 범위 내에 있고, 현재 largest보다 큰 경우
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # 오른쪽 자식이 힙 크기 범위 내에 있고, 현재 largest보다 큰 경우
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # largest가 현재 노드(i)와 다르다면 교환 필요
    if largest != i:
        # 현재 노드와 largest 위치의 값을 교환
        arr[i], arr[largest] = arr[largest], arr[i]
        # 교환된 자식 노드에서 다시 heapify를 수행하여
        # 최대 힙 속성 유지
        heapify(arr, n, largest)

# 힙 정렬
def heap_sort(arr):
    # 배열(리스트)의 길이
    n = len(arr)

    # 최대 힙 구성 단계
    # 마지막 비단말 노드부터 시작하여 루트까지
    # heapify 수행
    # (n // 2 -1)은 마지막 비단말 노드의 인덱스
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # 정렬 단계
    # 힙에서 최대값(루트)을 하나씩 꺼내어 배열 끝부터 채움
    for i in range(n - 1, 0, -1):
        # 루트(최대값)를 현재 힙의 마지막 요소와 교환
        arr[0], arr[i] = arr[i], arr[0]
        # 루트 노드에 대해 heapify를 수행하여 최대 힙 속성 복구
        # 이때 힙의 크기를 i로 제한하여 정렬된 부분은 제외
        heapify(arr, i, 0)
    # 정렬된 배열 반환
    return arr

if __name__ == "__main__":
    import random
    arr = [random.randrange(1, 100) for _ in range(10)]
    # print(arr)
    print(heap_sort(arr))









