def stockBuySell(self, A, n):
		#code here
		res = []
        check = 0
        for i in range(1,n):
            if (A[i] < A[i-1]):
                if check != i-1:
                    res.append((check,i-1))
                check = i
        if check != n-1:
            res.append((check,n-1))
        return res
