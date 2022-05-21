# swapping in python 

a = 5 
b = 6

#method 1
temp = a
a = b
b = temp
print(a,b)

#method 2
a = 5
b = 6

a = a + b  # 11
b = a - b   # 5
a = a - b   # 6
print(a,b)

# method 3   Use XOR 
a=5
b=6

a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

# method 4 
a = 5
b = 6

a,b = b,a
print(a,b)

