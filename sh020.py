p,r=map(int,input().split())
for k in range(p,r):
    if s>1:
        for i in range(2,s):
            if s%i==0:
                break
        else:
            print(s,end=" ")
