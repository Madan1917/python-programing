l =[]
list =[0,0]
n = int(input("Enter no of elements: "))

for i in range(0,n):
  l.append(int(input("Enter the Element: ")))

for i in l:
  if i%2==0:
    list[0]+=i**2
  else:
    list[1]+=i**2

print(f"List{list}")
