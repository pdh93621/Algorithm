def binary_search(array, target, start, end):
    # 만일 start > end 이면 종료!
    while start <= end:
        mid = (start + end) // 2
        # 타겟과 동일하면 리턴!
        if array[mid] == target:
            return mid
        # 타겟이 중간값보다 작으면 왼쪽 탐색
        elif array[mid] > target:
            end = mid - 1
        # 타겟이 중간값보다 크면 오른쪽 탐색 
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다')

else:
    print(result + 1)