w = int(input("Enter width: "))
h = int(input("Enter height: "))

for _ in range(h):
    print('*' * w)
    
print()

h = int(input("Enter the height of the triangles: "))

print()

# 1. Left aligned triangle
for i in range(1, h + 1):
    print('*' * i)

print()

# 2. Right aligned triangle
for i in range(1, h + 1):
    print(' ' * (h - i) + '*' * i)

print()

# 3. Triangle with spaces between stars
for i in range(1, h + 1):
    print(' ' * (h - i) + '* ' * i)
