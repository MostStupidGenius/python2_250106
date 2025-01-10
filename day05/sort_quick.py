# sort_quick.py
# 퀵 정렬
# 분할 정복 알고리즘의 한 종류로,
# "피벗"이라는 기준 원소를 선정하여
# 피벗보다 작은 값들은 왼쪽으로
# 피벗보다 큰 값들은 오른쪽 그룹으로 모아서
# 재귀적으로 퀵정렬을 시행한다.

# 퀵 정렬 구현
def quick_sort(arr: list):
    # 기본 케이스: 리스트의 길이가 1이면 그대로 반환
    if len(arr) <= 1:
        return arr
    
    # 피벗 선택
    # 일반적으로 중간 요소를 선택한다.
    # 전체 길이를 2로 나눈 몫을 선택한다.
    # pivot = arr[len(arr) // 2]
    pivot = arr[0]

    # 피벗을 기준으로 리스트를 세 부분으로 분할
    left = [x for x in arr if x < pivot] # 피벗보다 작은 요소들
    middle = [x for x in arr if x == pivot] # 피벗과 같은 요소들
    right = [x for x in arr if x > pivot] # 피벗보다 큰 요소들

    # 분할된 리스트를 재귀적으로 정렬하고 병합
    result = quick_sort(left) + middle + quick_sort(right)
    # print(f"{quick_sort(left)} + {middle} + {quick_sort(right)}")
    return result

if __name__ == "__main__":
    import random
    arr = [3, 6, 8, 10, 1, 2, 1]
    # 1부터 100까지의 수 중 10개를 임의로 골라서 리스트를 만드는 코드
    arr = [random.randrange(1, 100) for _ in range(10)]
    # 초기 리스트 확인
    print(arr)
    print()
    # 퀵정렬 시행
    result = quick_sort(arr)
    print(result)








