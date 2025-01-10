# sort_insertion.py
# 삽입 정렬
# 좌측의 정렬후와 우측의 정렬전으로 나누어
# 정렬전의 첫번째 원소를 정렬후의 적절한 위치에 삽입하는
# 방식을 취한다.
def insertion_sort(arr):
    # 0번째 원소는 이미 정렬되었다고 판단하여
    # 1번째부터 정렬을 진행한다.
    for i in range(1, len(arr)):
        # 현재 삽입할 값
        key = arr[i]
        # 현재 값의 이전 위치
        j = i-1

        # 현재 값보다 큰 값들을 오른쪽으로 이동
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        # 알맞은 위치에 현재 숫자 삽입
        arr[j+1] = key
        print(i, arr)
    return arr


if __name__ == "__main__":
    arr = [65, 34, 26, 12, 24, 11, 90]
    print("원래 배치: \n", arr)
    sorted_arr = insertion_sort(arr)
    print("삽입 정렬 결과: ", sorted_arr)