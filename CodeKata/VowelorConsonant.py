x=input()
c = ['a','e','i','o','u','A','E','I','O','U']
if (x is c):
  print("Vowel")
elif (x not in c):
  if((x>'A' and x<'Z') or (x>'a' and x<'z')):
    print("Consonant")
  else:
    print("invalid")
