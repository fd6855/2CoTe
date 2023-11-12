N = int(input())
fac = list(map(int, input().split()))

fac.append(0)
fac.append(0)
idx = 0
cost = 0

for idx in range(N):
  if fac[idx + 1] > fac[idx + 2]:
    tmp = min(fac[idx], fac[idx + 1] - fac[idx + 2])
    cost += tmp * 5
    fac[idx] -= tmp
    fac[idx + 1] -= tmp
    tmp2 = min(fac[idx], min(fac[idx + 1], fac[idx + 2]))
    cost += tmp2 * 7
    fac[idx] -= tmp2
    fac[idx + 1] -= tmp2
    fac[idx + 2] -= tmp2
  else:
    tmp = min(fac[idx], min(fac[idx + 1], fac[idx + 2]))
    cost += 7 * tmp
    fac[idx] -= tmp
    fac[idx + 1] -= tmp
    fac[idx + 2] -= tmp
    tmp2 = min(fac[idx], fac[idx + 1])
    cost += 5 * tmp2
    fac[idx] -= tmp2
    fac[idx + 1] -= tmp2
  cost += 3 * fac[idx]

print(cost)
