#User function Template for python3

from collections import *
class Solution:
    def canPair(self, arr, k):
        for i in range(len(arr)):
            arr[i]%=k
        c = Counter(arr)
        print(c)
        for x in c:
            if x == 0 and c[0]%2!=0:
                return False
            if x!=0 and c[x]!=c[k-x]:
                return False
        return True
		    
		     


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, k = input().split()
		n = int(n)
		k = int(k)
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.canPair(nums, k)
		if(ans):
			print("True")
		else:
			print("False")
# } Driver Code Ends
