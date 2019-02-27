# your code goes here\
b=[]
n=int(input())
for i in range(0,n):
    a=int(input())
    b.append(a)
for i in range(1,100000):
    if((b.count(i))>1):
        print(i)
    else:
        print("unique")
        break
