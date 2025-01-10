# sort_bubble.py
# 정렬
# 왼쪽은 작은 값, 오른쪽은 큰 값으로 오름차순 정렬을
# 기준으로 한다.

# 버블 정렬
# 모든 요소의 가장 왼쪽에서부터 두 원소를 비교하여
# 정렬(교환)한다.
# 이를 가장 마지막 원소까지 반복하고
# 교환이 일어나지 않을 때(정렬완료)까지
# 무한히 반복한다.
def bubble_sort(arr: list) -> list:
    # 리스트 요소의 개수를 변수에 담아둔다.
    arr_length = len(arr)
    
    # 리스트 요소의 개수만큼 반복을 한다.
    for i in range(arr_length):
        # 최적화: 이미 정렬된 경우, 조기 종료
        swapped = False # 교환이 발생한지 여부

        # 각 패스마다 끝에서부터 i+1개의 원소는
        # 이미 정렬되어 있으므로 arr_length-(i+1)까지만 비교
        for j in range(0, arr_length-(i+1)):
            # 인접한 두 원소를 비교하여
            # 순서가 잘못되어 있으면 교환
            if arr[j] > arr[j+1]:
                # 두 원소를 교환
                arr[j], arr[j+1] = arr[j+1], arr[j]

                # 파이썬스럽지 않은 방식
                # dummy = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] = dummy
                # print(f"i:{i} j:{j}\narr: {arr}\n") 

                # 교환이 일어났으므로 True로 변경
                swapped = True
        # 전체 순환 후 교환이 발생하지 않았다면
        # 정렬된 상태이므로, 조기 종료
        if swapped is False:
            break
    # 전달받은 arr을 정렬한 후 정렬된 상태로 반환
    return arr

if __name__ == "__main__":
    arr = [65, 34, 26, 12, 24, 11, 90]
    print("원래 배치: ", arr)
    sorted_arr = bubble_sort(arr)
    print("버블 정렬 결과: ", sorted_arr)