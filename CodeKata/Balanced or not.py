x=input()
c=[]
for i in range (len(x)):
  if(x[i]=='('):
    c.append(x[i])
  else:
    c.pop()
if(len(c)==0):
  print('yes')
else:
  print('no')
