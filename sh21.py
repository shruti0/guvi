def fact(r):
  return 1 if (r==1 or r==0) else r*fact(r-1)
r = int(input())
p = fact(r)
print(p)
