#print N to 1

def printNto1(n):
    if n <= 1:
        print(n)
        return
    else:
        print(n)
        n-=1
        printNto1(n)
        
printNto1(100)
    