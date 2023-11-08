N, M, K = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
res = 0
i = 0
while i < M:
  for j in range(K):
    res += num[N - 1]
    i += 1
  res += num[N - 2]
  i += 1
print(res)
