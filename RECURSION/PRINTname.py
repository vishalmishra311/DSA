# two variable n and name , print names n times using these two varibale 
def printNames(names , n):
    if (n==0):
        return
    print (names,"->",n)
    printNames(names , n-1)

names = input("enter the name:")
n = int(input("enter the number-->"))
printNames(names,n)
    
### using backtracking  
def printNames(names , n):
    if (n==0):
        return
    printNames(names , n-1)
    print (names,"->",n)
names = input("enter the name:")
n = int(input("enter the number-->"))
printNames(names,n)
    