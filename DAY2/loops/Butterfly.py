n = 4   
#upper part
for i in range(1, n+1):
    #left
    for j in range(1,i+1):
        print("*" , end="")
    
    #spaces
    for j in range(1,2*(n-i)+1):
        print(" ",end="")

    #right
    for j in range(1,i+1):
        print("*",end="")
    print()
    
#lower part
for i in range(n,0,-1):
    #left
    for j in range(1,i+1):
        print("*" , end="")
    
    #spaces
    for j in range(1,2*(n-i)+1):
        print(" ",end="")

    #right
    for j in range(1,i+1):
        print("*",end="")
    print()