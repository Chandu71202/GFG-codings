#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
       jm = {}
       s=0
       r=0
       for i in range(n):
           s+=arr[i]
           if s==0:
               r=max(r,i+1)
           elif s in jm:
               r=max(r,i-jm[s])
           else:
               jm[s]=i
       return r
