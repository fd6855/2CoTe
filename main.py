A=input()
B=input()
while len(A)<len(B):
  if A!=B:
    if B[-1]=="A":
      B=B[:-1]
    else:
      B=B[:-1]
      B=B[::-1]
if A==B:
  print("1")
else: print("0")
