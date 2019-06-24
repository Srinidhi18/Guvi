x=['a','e','i','o','u','A','E','I','O','U']
a=input()
for i in a:
  if i in x:
    c=0
  else:
    c=1
if c==0:
  print('yes')
else:
  print('no')
