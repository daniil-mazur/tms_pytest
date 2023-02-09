from triangle.triangle import Triangle

first = Triangle(4, 5, 6)
second = Triangle(4, 5, 6)
# second = first

third = Triangle

print(id(first))
print(id(second))
print(id(Triangle(5, 6, 7)))
# print(id(third))
print(id(Triangle))
print(id(isinstance))

# print(first == second)
# print(first is second)
# print(id(first) == id(second))
