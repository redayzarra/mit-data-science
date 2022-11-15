#THE KNAPSACK PROBLEM - Optimization Models

#Optimization models are great for finding the fastest, biggest, etc. 

#Part 1 - Objective function that is to be maximized or minimized
#Part 2 - A set of constraints that must be honored

#Takeaways: Many real life problems can be formulated into an optimization model
           #Reduce a new problem with methods of how old problems were solved
           #Optimization problems are computationally complex and hard
           #Greedy algorithim to find a "good-enough" solution

#Knapsack Problem - you have a backpack with limited space and you want to fit 
                   #as much valuable items as possible. What will you take?

    #Whole Variant - you cannot take portions of an item, such as a painting
    #Continuous Variant - you can take portions, such as liquid gold

#The whole variant problem is a lot harder than the continuous one.

#Whole Problem Formalized:
    #Each item is represented by a pair, <value, weight>
    #Knapsack can't take more than a total weight of W
    #Vector(L) of length (n) is a set of the items. Each element is an item
    #Vector(V) of length (n) to indicate if the item is taken, V[i] = 1 meaning
    #the item has been taken. V[i] = 0 to show that the item is not taken.

    #Formalized Problem: Find a vector (V) so that the each item (i) multiplied 
    #by the value of the item is the greatest value. While also being less than
    #or equal to total weight (W)

#Brute Force Algorithim:
    #Enumerate all possible combinations of the item. Essentially, generate all
    #subsets of the given set or power set.
    #Remove all combinations that exceed the total weight (W)
    #From the viable options, choose the one with the most value

    #Not very practical even though it will provide us with the most optimal
    #solution every time. Takes a lot of time and space.

#The Knapsack Problem is inherently exponential. Meaning there is no algorithim
#that can solve it faster than that. However, there are "good" ways of solving
#the problem that can provide approximate solutionns or even optimal solutions.

#Greedy Algorithim: