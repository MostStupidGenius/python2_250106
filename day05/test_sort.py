# test_sort.py
# 시간복잡도 측정

import os
import sys
from sort_merge import merge_sort
from sort_quick import quick_sort
folder_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(folder_path)
from day04.sort_bubble import bubble_sort
import time

# 리스트와 함수(정렬)를 전달받아
# 시작시간 출력 후
# 해당 함수로 정렬 시작,
# 결과가 나온 시간을 출력
def test_sort(arr:list, sorter):
    before = time.time()
    sorter(arr)
    times = time.time()-before
    print(f"{times:.3f}")

if __name__ == "__main__":
    import random
    arr = [random.randrange(1, 1000) for _ in range(1000)]
    print("bubble sort:")
    test_sort(arr, bubble_sort)
    print("merge sort:")
    test_sort(arr, merge_sort)
    print("quick sort:")
    test_sort(arr, quick_sort)
