#User function Template for python3

class Solution:
    def noOfWays(self, M, N, X):
        # code here
        dp=[[0 for j in range(X+1)] for i in range(N)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0 and j<=M and j!=0:
                    dp[i][j]=1
                elif i==0 and j>M:
                    dp[i][j]=0
                else:
                    a = 0 if j<=M else j-M
                    dp[i][j]=sum(dp[i-1][a:j])
                    
        return dp[-1][-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        M,N,X=map(int,input().split())
        
        ob = Solution()
        print(ob.noOfWays(M,N,X))
# } Driver Code Ends
