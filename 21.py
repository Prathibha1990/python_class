# intersection and Difference
set1={1,34,5,56,78,89,89,987}
set2={2,4,5,67,56,78,45,45}

print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))
# & is a intersection
# | is  a union
# - is difference (symetric)
print(set2.union(set1))

# symetric ^
print(set2.difference(set1))
