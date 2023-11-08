N, M = map(int, input().split())
card = [[0 for _ in range(M)] for _ in range(N)]
res = 0
for i in range(N):
  card[i] = list(map(int, input().split()))
  if res < min(card[i]):
    res = min(card[i])
print(res)
