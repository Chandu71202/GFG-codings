class Solution:
	def digitsNum(self, N):
		s=""
    	if (N == 0) :
    	    s="0"
    
    	if (N % 9 != 0):
    	    s=s+str(N%9)
    
    	for i in range( 1, int(N / 9) + 1) :
    	    s=s+"9"
    
    	for i in range(1, N + 1) :
    	    s=s+"0"
    	    
    	return s 
