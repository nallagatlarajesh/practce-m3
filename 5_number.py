n=5
for i in range(1,n+1):               # first iteration data in below comments 
    space = (n-i)*""               #n=5  i=1   n-i=4    4*" "="    " =4 space
    for k in range(i,1,-1):         #i=1
        print(k,end=" ")           # k=1
    #this for loop will print the increasing numbers
    for j in range(1,i+1):         #from 1 to 1
        print(j, end =" ")         #j=1
    print()
