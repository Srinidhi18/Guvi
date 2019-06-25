x=['a','e','i','o','u','A','E','I','O','U']
d=input()
b=0
for i in d:
  if i in x:
    b=0
if b==0:
  print('yes')
else:
  print('no')
