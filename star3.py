n=3
for i in range(1,n+1):
    #this will print the space
    space=(n-i)*" "       #n=3   i=1   n-i=2   2*" "=  2 space
    #it will print the star
    star = (2*i -1)*"*"    #i=1   2*1-1=1   1*"*"=   "*" = 1 star
    print(space,star)
for j in  range (n-1,0,-1):
    space = (n-j)*" "   #n=3 j=2   n-j=1  1*""=  1 space
    star=(2*j-1)*"*"    #j=2    2*2-1=3    3*"*"="***"   =3 stars
    print(space,star)
    
