N = int(input())

soldier = list(map(int, input().split()))

dp = [1] * N

for n in range(1,N):
    for i in range(n):
        if soldier[i] > soldier[n]:
            dp[n] = max(dp[n], dp[i] + 1)

print(N - max(dp))