#  Sets in Python
'''
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5, 6}

'''
set1 = {1,2,3}
set2 = {4,5,6}
print(set1)  # Output: {1, 2, 3}

# Union of sets
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection of sets
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: set() (empty set, no common elements)

# Difference of sets
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2, 3} (elements in set1 not in set2)