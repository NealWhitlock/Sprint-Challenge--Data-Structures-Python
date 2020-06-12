import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


""" ORIGINAL CODE (7.3 seconds)"""
# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)


""" MY CODE USING BINARY SEARCH TREE (0.1 seconds)"""
# # Initialize a binary search tree with first name in list 1
# names_bst = BSTNode(names_1[0])

# # Insert each name from list 1 into BST
# for i in range(1,len(names_1)):
#     names_bst.insert(names_1[i])

# # Loop through names in list 2 to check if they are contained in 
# # list 1's BST and append to duplicates list if so
# for name in names_2:
#     if names_bst.contains(name):
#         duplicates.append(name)


""" USING PYTHON TOOLS WITHOUT RESTRICTIONS (0.006 seconds)"""
# # Using Python sets to get the intersection
# duplicates = list(set(names_1) & set(names_2))


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
