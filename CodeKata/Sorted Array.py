x= int(input())
if(x>1 and x<1000):
  l=list(map(int,input().split()))
  s=sorted(l)
for i in range (0,len(s)):
  print(s[i],end = ' ')
  

