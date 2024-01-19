str = input()
result = ""
for i in str:
    if i.islower():
        result = result + i.upper()
        

    elif i.isupper():
        result = result + i.lower()

print(result)


    


#aBcDeFg