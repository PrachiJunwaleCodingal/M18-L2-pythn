#reverse the string

str1 = input("Please enter string : ")
str2 = ('')
for i in str1:
    str2 = i + str2
    
print("The Reversed string : ", str2)
