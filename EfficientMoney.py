N, M = list(map(int, input().split()))

value = []
for _ in range(N):
    value.append(int(input()))

array = [10001]*(M+1)

array[0] = 0
for i in range(N):
    for j in range(value[i], M + 1):
        if array[j - value[i]] != 10001:
            array[j] = min(array[j], array[j - value[i]] + 1)

if array[M] == 10001:
    print(-1)
else:
    print(array[M])

