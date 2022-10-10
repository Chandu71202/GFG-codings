#User function Template for python3

class Solution:
    def count(self, candidates, N, target):
        # code here 
        dp = [[1]+[0]*(sum) for i in range(N+1)]
        for i in range(1,N+1):
            for j in range(sum+1):
                if coins[i-1]<=j:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                     dp[i][j] = dp[i-1][j]
        return dp[-1][-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        sum,N = list(map(int, input().strip().split()))
        coins = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(coins,N,sum))

# } Driver Code Ends
