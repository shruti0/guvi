pr=int(input())
sum=0
t=pr
while t>0:
  digit=t%10
  sum+=digit**3
  t//=10
if pr==sum:
  print("yes")
else:
  print("no")
