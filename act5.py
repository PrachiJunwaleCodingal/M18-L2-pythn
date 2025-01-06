#Number of words-
str1 = input(" Enter a sentence: ")
num = 1 

for i in range(len(str1)): 
    if(str1[i] == ' ' ):
       num = num + 1

print("Total Number of Words= ",num)

