n=int(input("enter number:"))

n1=0
n2=1
print("fibinacci series:")
print(n1)
temp=0
for i in range(n-1):
    print(n2)
    temp=n2
    n2=n1+n2
    n1=temp
    