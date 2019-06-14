import re
a= input()
d= len(a)-len(re.findall('[\w]',a))
print(d)
