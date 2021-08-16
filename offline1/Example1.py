n=int(input("enter number:"))
temp=n*2-1
for i in range(1,n+1):
    u=n-i
    m=temp-((n-i)*2)
    print(""+" "*(n-i),"*"*m)
    
for i in range(1,n):
    u=n-i
    m=temp-(i*2)
    print(""+" "*(i),"*"*m)