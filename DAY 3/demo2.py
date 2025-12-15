s = input("Enter a string: ")

print("\nOriginal String:", s)
# Basic slicing
print("s[0:5]  ->", s[0:5])     
print("s[:5]   ->", s[:5])      
print("s[2:]   ->", s[2:])      
print("s[:]    ->", s[:])       

# Negative indexing
print("s[-5:]  ->", s[-5:])     
print("s[:-5]  ->", s[:-5])     

# Step slicing
print("s[::2]  ->", s[::2])     
print("s[1::2] ->", s[1::2])   

# Reverse string
print("s[::-1] ->", s[::-1])   