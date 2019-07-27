x=int(input())
c=1
a=list(map(int,input().split()))
for i in range (len(a)):
  if(i==a[i]):
    print(a[i],end=' ')
    c=c+1

if(c==1):
  print('-1')
