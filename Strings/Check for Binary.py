def isBinary(str):
    #code here
    # a=list(set(str))
    # if(len(a)==1 and a[0]=='0' or a[0]=='1'):
    #     return True
    # elif(len(a)==2 and a==['0','1'] or a==['0','0'] or a==['1','1']):
    #     return True
    # else:
    #     return False
    try:
        n=int(str,2)
        return 1
    except:
        return 0
