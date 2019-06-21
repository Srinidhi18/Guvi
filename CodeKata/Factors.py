x=int(input())
c=[x]
if(x<=1000):
  for i in range(1,x+1):
    if(x%i==0):
        print(i,end=' ')
  
  
