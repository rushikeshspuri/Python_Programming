
a = 10
b = 10

print(id(a))
print(id(b))

a = [10]
b = [10]

print(id(a))
print(id(b))

# Visualizing the Memory DifferenceFor Integers:a ➔ [ Memory Box: 10 ] 
# b (Both look at one box)
# For Lists:a ➔ [ Memory Box 1: [10] ]
# b ➔ [ Memory Box 2: [10] ] (Two separate boxes)
