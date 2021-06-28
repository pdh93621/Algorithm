def binary_search(array, target, start, end):
    
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 위치 반환
    if array[mid] == target:
        return mid
    
    # 중간 기준으로 타겟이 작으면 왼쪽 아니면 오른쪽
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
        return binary_search(array, target, mid+ 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)