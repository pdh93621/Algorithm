from bisect import bisect_left

N,M = list(map(int, input().split()))

length = list(map(int, input().split()))

length.sort()
sums = []

for cut in range(length[-1], 0, -1):
    sum = 0
    for l in length:
        if l > cut:
            sum += l - cut
    sums.append(sum)

print(length[-1] - bisect_left(sums, M))
