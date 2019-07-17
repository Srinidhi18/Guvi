a=input()
for i in a:
  if(i=='/'):
    c=a.split('/')
    print(int(int(c[0])/int(c[1])))
  elif (i=='%'):
    c=a.split('%')
    print(int(int(c[0])%int(c[1])))
