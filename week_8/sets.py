#Sets

my_set = {1, 2, 3, 4, 5, 6}
print(my_set)

my_set.add(7)
print(my_set)

my_set.remove(4)
print(my_set)

#Operations with sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union Adds both sets together and removes any duplicates

union_set = set1.union(set2)
print(union_set)

# Intersection Find duplicates in the sets

inter_set = set1.intersection(set2)
print(inter_set)

# Difference Finds the elements that are present in one but not the other 

diff_set = set1.difference(set2)
diff_set2 = set2.difference(set1)
print(diff_set)
print(diff_set2)