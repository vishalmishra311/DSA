# print names 5 times using recursion 

def multipleSameName(name):
    #print ( "name in line 4",name)
    if name == 6:
        return 
    else:
        print("vishal")
        print ( "name in line 9->",name)
        multipleSameName(name+1)
        
multipleSameName(0) 