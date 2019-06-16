x=input()
a=False
b=False
for i in x:
  if(i.isalpha()):
    a=True
  if(i.isdigit()):
    b=True
if(a==True and b==True):
  print('Yes')
else:
  print('No')


