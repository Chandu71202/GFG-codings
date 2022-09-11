def findFloor(self,A,N,X):
        #Your code here
        l=[]
        for i in A:
            if i<=X:
                l.append(i)
            else:
                break
        if l==[]:
            return -1
        return A.index(l[-1])
        
