x=int(input())
a=list(input().split())
c=min(set(a), key = a.count) 
print(c)
