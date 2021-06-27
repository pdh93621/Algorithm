N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

for k in range(K):
    if A[k] < B[N-k-1]:
        A[k] = B[N-k-1]
    else:
        break

print(sum(A))
