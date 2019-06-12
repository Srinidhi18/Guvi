a,b= map(int,input().split())
d=0
x=list(map(int,input().split()))
if(len(x)==a):
  for y in range (0,b):
     d=d+x[y]
  print(d)
else:
  exit()
