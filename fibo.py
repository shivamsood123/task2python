n = int(input("Enter the number of terms required: "))
f = 0  # first term 
s = 1  # second term 
sum = 0
count = 1
print("Fibonacci Series is : ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  f = s
  s = sum
  sum = f + s
