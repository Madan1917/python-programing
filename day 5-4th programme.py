n = []
while True:
  s = input()
  if s =='*':
    break
  else:
    n.append(int(s))

for j in n:
  if j>=1 and j<=(10**9):
    prod = 1
    sumi = 0
    for i in range(1,j+1):
      prod*=i
      sumi+=i
    if prod%sumi == 0:
      print("YEAH")
    else:
      print("NAH")
