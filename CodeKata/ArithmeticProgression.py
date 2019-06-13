n,a,d=map(int,input().split())
s=0
for i in range(1,n+1):
  sum=a+((i-1)*d)
  s=s+sum   
print(s)
