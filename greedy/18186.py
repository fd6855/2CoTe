N, B, C = map(int, input().split())
fac = list(map(int, input().split()))

fac.append(0)
fac.append(0)
idx = 0
cost = 0

for idx in range(N):
  if B > C:
    if fac[idx + 1] > fac[idx + 2]:
      tmp = min(fac[idx], fac[idx + 1] - fac[idx + 2])
      cost += tmp * (B + C)
      fac[idx] -= tmp
      fac[idx + 1] -= tmp
      tmp2 = min(fac[idx], min(fac[idx + 1], fac[idx + 2]))
      cost += tmp2 * (B + C * 2)
      fac[idx] -= tmp2
      fac[idx + 1] -= tmp2
      fac[idx + 2] -= tmp2
    else:
      tmp = min(fac[idx], min(fac[idx + 1], fac[idx + 2]))
      cost += (B + C * 2) * tmp
      fac[idx] -= tmp
      fac[idx + 1] -= tmp
      fac[idx + 2] -= tmp
      tmp2 = min(fac[idx], fac[idx + 1])
      cost += (B + C) * tmp2
      fac[idx] -= tmp2
      fac[idx + 1] -= tmp2
    cost += B * fac[idx]
  else:
    cost += fac[idx] * B

print(cost)
