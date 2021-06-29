T = int(input())

for _ in range(T):
    N, M = list(map(int, input().split()))
    temp = list(map(int, input().split()))

    mine = []

    for n in range(N):
        mine.append([i for i in temp[n*M:(n+1)*M]])

for m in range(1,M):
    for n in range(N):
        if n == 0:
            left_up = 0
        else:
            left_up = mine[n-1][m-1]
        if n == N - 1:
            left_down = 0
        else:
            left_down = mine[n+1][m-1]
        left = mine[n][m-1]
        mine[n][m] += max(left_up, left_down, left)

#print(mine)

result = 0
for n in range(N):
    result = max(result, mine[n][M-1])

print(result)


