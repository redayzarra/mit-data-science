# BRUTE FORCE ALGORITHMS - Optimization Problems, Lecture 2, Segment 1

# Greedys are easy to implement and very efficient but do not provide the most
# optimal solution. 

# Brute Force Algorithm: 
#   1. Enumerate all possible combinations of items.
#   2. Remove all of the combinations that exceed the total weight.
#   3. Choose any whose value is the largest

#Search Tree Implementation:
#   1. The tree is built top down starting with the root
#   2. The first element is selected from the still to be considered items.            
#         - If there is room for an item, a node is constructed to show 
#           what would happen from taking that item. We draw that as the 
#           left child. 
#         - We also explore consequences of not choosing the item, right child.
#   3. We can apply the process recursively to the non-leaf children