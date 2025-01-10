# sort_merge.py
# 병합 정렬
# 리스트를 절반으로 나눠서
# 각 부분 리스트를 재귀적으로 정렬
# 정렬된 부분 리스트들을 병합하여 전체 리스트 정렬

# 병합 정렬 구현
def merge_sort(arr:list):
    # 기본 케이스: 리스트의 길이가 1 이하면 그대로 반환
    if len(arr) <= 1: return arr

    # 리스트를 두 부분으로 나눔
    mid = len(arr) // 2

    # 왼쪽 리스트 재귀 호출
    left = merge_sort(arr[:mid])
    # 오른쪽 리스트 재귀 호출
    right = merge_sort(arr[mid:])

    # 정렬된 두 부분 리스트를 병합과 함께 정렬
    result = merge(left, right)
    return result

def merge(left, right):
    # 결과 반환을 위한 변수
    result = []
    # 두 리스트를 비교하기 위한 인덱스 변수들
    i, j = 0, 0

    # 두 리스트를 비교하며 작은 값을 result에 추가
    while i < len(left) and j < len(right):
        # 만약 왼쪽 리스트의 i번째 값이
        # 오른쪽 리스트의 j번째 값보다 작거나 같다면
        if left[i] <= right[j]:
            # left[i] 값을 result에 추가
            result.append(left[i])
            # i 인덱스 증가
            i += 1
        else:
            result.append(right[j])
            j += 1

    # while문 탈출 후
    # 남은 요소들을 result에 추가
    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == "__main__":
    import random
    arr = [13, 5, 2, 10, 9, 7, 1]
    arr = [random.randrange(1, 200) for _ in range(100)]
    result = merge_sort(arr)
    print(result)