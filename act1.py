#Sum of whole numbers
n = int(input("Enter the number to find the sum: "))
sum=0
for i in range(1, n+1):
  sum = sum+i
  print("Sum =", sum)