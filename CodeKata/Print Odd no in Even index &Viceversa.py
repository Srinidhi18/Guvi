x=int(input())
c=[]
a=list(map(int,input().split()))
for i in range (len(a)):
  if(i%2==0):
    if(a[i]%2!=0):
      print(a[i],end=' ')
  if(i%2!=0):
    if(a[i]%2==0):
      print(a[i],end=' ')
      
      
