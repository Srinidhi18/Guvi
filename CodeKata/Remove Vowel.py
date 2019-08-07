x=int(input())
a=input()
c=['a','e','i','o','u','A','E','O','I','U']
b=[]
for i in range(len(a)):
  if(a[i] not in c):
    b.append(a[i])
k=b[::-1]
for i in range(len(k)):
     print(k[i],end='')
