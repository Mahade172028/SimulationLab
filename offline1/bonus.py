def calculate(n):
    a=0
    while n!=0:
        a=a+n%10
        n=int(n/10)
    return a

n=int(input("enter number:"))

while 1:
    if int(n/10)==0:
        break
    n=calculate(n)
    
print(n)
    