p,r=map(list,input().split())
cou=0
if(len(p)==len(r)):
    for i in range(0,len(p)):
        if(p[i]==r[i]):
            continue
        else:
            cou=cou+1
if(cou==1):
    print("yes")
else:
    print("no")
© 2019 GitHub, Inc.
