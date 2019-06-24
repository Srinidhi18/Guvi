x=['a','e','i','o','u','A','E','I','O','U']
c=input()
b=0
for i in c:
  print(i)
  if i in x:
    b=0
if b==0:
  print('yes')
else:
  print('no')
