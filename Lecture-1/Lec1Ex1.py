# UNIT 1 - Lecture 1: Excercise 1

# 1. Metric 1:
def metric1(item):
    return item.getValue() / item.getWeight() 

# Which heuristic does Metric 1 employ?

# Choose the lightest object first.
# Choose the most valuable object first.
# Choose the item with the best value to weight ratio first. [X] Correct.

# What will be the result of running the burgler's algorithm with Metric 1?

# The algorithm runs and returns the optimal solution.
# The algorithm runs and returns a non-optimal solution.
# The algorithm does not run. [X] Correct.

###############################################################################

# 2. Metric 2:
def metric2(item):
    return  -item.getWeight()

# Which heuristic does Metric 2 employ?

# Choose the lightest object first. [X] Correct.
# Choose the most valuable object first.
# Choose the item with the best value to weight ratio first.

# What will be the result of running the burgler's algorithm with Metric 2?

# The algorithm runs and returns the optimal solution.
# The algorithm runs and returns a non-optimal solution. [X] Correct.
# The algorithm does not run.

###############################################################################

# 3. Metric 3:
def metric3(item):
    return item.getValue()

# Which heuristic does Metric 3 employ?

# Choose the lightest object first.
# Choose the most valuable object first. [X] Correct.
# Choose the item with the best value to weight ratio first.

# What will be the result of running the burgler's algorithm with Metric 3?

# The algorithm runs and returns the optimal solution.
# The algorithm runs and returns a non-optimal solution. [X] Correct.
# The algorithm does not run.