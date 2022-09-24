def num_pattern(n):
   num=int(input("enter the starting number"))
   for i in range(1,n+1):
      for j in range(i):
         print(num,end=" ")
         num+=1
      print()
print("Enter number of rows")
r=int(input())
num_pattern(r)
