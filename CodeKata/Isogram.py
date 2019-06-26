x=input()
def is_isogram(word): 

    c = word.lower() 
    letter_list = [] 
    for i in c: 
  
        if i.isalpha(): 
            if i in letter_list: 
                return("No")
            letter_list.append(i) 
  
    return ("Yes")
c=is_isogram(x)
print(c)
