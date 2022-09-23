s = input("Enter string: ")
k = int(input("k: "))
dict = {x:s.count(x) for x in s}
sum = 0

for i in dict.values():
  if i > k:
    sum+=i

print(sum)
