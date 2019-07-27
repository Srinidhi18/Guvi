x,y=map(int,input().split())
a=list(input().split())
c=[]
for i in range(len(a)):
  if(int(a[i])%2!=0):
    if a[i] not in c:
      c.append(a[i])
print(c[y-1])
