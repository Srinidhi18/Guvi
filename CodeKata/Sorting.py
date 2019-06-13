a= int(input())
if(a>1 and a<100000):
  x=list(map(int,input().split()))
  sl=sorted(x)
for i in range (0,len(sl)):
  print(sl[i],end = ' ')
