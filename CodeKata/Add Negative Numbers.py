a=int(input())
b=list(input().split())
c=0
k=0
for i in range(len(b)):
  if(int(b[i])<0):
    c=c+int(b[i])
    print(c) 
  else:
    k=k+1
if(c==0):
  print('0')




