import re
x= input()
c= len(x)-len(re.findall('[\w]',x))
print(c)
