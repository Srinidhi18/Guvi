a= int(input())
if(a>1 and a<1000):
  l=list(map(int,input().split()))
  avg=sum(l)/len(l)
  print(int(avg))
