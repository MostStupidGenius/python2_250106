# sort_selection.py
# 선택 정렬 O(n^2)
# 정렬된 좌측의 작은 값들이 들어간 부분(정렬후)과
# 우측의 정렬되지 않은 부분(정렬전)으로 나누고
# 정렬전 원소 중 가장 작은 원소를 순회를 통해 찾아
# 정렬후의 뒤에 붙인다.

def selection_sort(arr: list) -> list:
    # 리스트의 길이를 가져온다.
    arr_length = len(arr)

    for i in range(arr_length):
        # 현재 위치를 최소값의 인덱스로 초기화
        min_idx = i
        # i+1부터 끝까지 순회하며 최소값의 인덱스 찾기
        for j in range(i+1, arr_length):
            # 만약 j번째의 값이 min_idx번째의 값보다 작다면
            if arr[j] < arr[min_idx]:
                # j를 가장 작은 값을 가진 인덱스로 설정
                min_idx = j
        # 현재 위치의 원소 인덱스와 가장 작은 원소의 인덱스가
        # 같다면 다음 반복으로 이동
        if min_idx == i: continue
        # 현재 위치(i)의 원소와 찾은 최소값을 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"i: {i}, j: {j}\n{arr}\n")
    return arr

if __name__ == "__main__":
    arr = [23, 10, 49, 25, 75]
    print(arr)
    sorted_arr = selection_sort(arr)
    print("선택 정렬 결과: ", sorted_arr)