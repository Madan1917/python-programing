h = int(input("Enter number: "))
count=0
class Solution(object):
  def numSquares(n):
    from math import ceil, sqrt
    dp = [0, 1, 2, 3]
    if n<=3:
      return dp[n]
    else:
      for i in range(4, n + 1):
        dp.append(i)
        for x in range(1, int(ceil(sqrt(i))) + 1):
          temp = x*x
          if temp>i:
            break
          else:
            dp[i] = min(dp[i], 1 + dp[i - temp])
    return dp[n]
s = Solution
print(s.numSquares(h))
