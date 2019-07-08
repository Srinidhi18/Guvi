import math

x,y=map(int,input().split())
c=x*y
a=math.sqrt(c)
if(c==(a*a)):
  print('yes')
else:
  print('no')
