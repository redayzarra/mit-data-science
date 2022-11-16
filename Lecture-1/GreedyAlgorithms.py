# GREEDY ALGORITHMS - Optimization Problems, Lecture 1, Segment 2

# Greedy Algorithm a Practical Alternative:
#            While the knapsack is not full: Put "best" available item inside

# What does it mean to add the "best" item?
#            Most valuable? Least expensive? Highest value to units ratio?

# An example, you want to eat good food that satisfies you but you cannot exceed 
# a certain number of calories. 

# Let's build a program off the example by starting with the food:
class Food(object):
  def __init__(self, n, v, w):
    self.name = n
    self.value = v
    self.calories = w

    def getValue(self):
      return self.value

    def getCost(self):
      return self.calories

    def density(self):
      return self.getValue() / self.getCost()

    def __str__(self):
      return self.name + ': <' + str(self.value) / + ', ' + str(self.calories) + '>'

# To build the menu we can utilize this simple code:
def buildMenu(names, values, calories):
  """names, values calories lists of same length.
     name a list of strings
     values and calories lists of numbers
     returns list of foods"""
  menu = []
  for i in range(len(values)):
    menu.append(Food(names[i], values[i], calories[i]))
  return menu

#Implementation of a Flexible Greedy Algorithm
def greedy(items, maxCost, keyFunction):
  """Assumes items a list, maxCost >= 0,
        keyFunction maps elements of items to numbers"""
  itemsCopy = sorted(items, key = keyFunction,
                     reverse = True)
  result = []
  totalValue, totalCost = 0.0, 0.0

  for i in range(len(itemsCopy)):
    if (totalCost + itemsCopy[i].getCost()) <= maxCost:
      result.append(itemsCopy[i])
      totalCost += itemsCopy[i].getCost()
      totalValue += itemsCopy[i].getValue()

  return (result, totalValue) 

# We are using a Greedy Algorithm because we are concerned with efficiency and 
# do not want to use too much time or space.

# Lets use the Greedy Algorithm in a test! I will use comments next to the code
# to explain what every line does for my own personal understanding.

def testGreedy(items, constraint, keyFunction): #The function takes three arguments
  taken, val = greedy(items, constraint, keyFunction) #Calls the Greedy
  print("Total value of items taken =", val) #Prints the final result
  for item in taken:
    print ("   ", item)

def testGreedys(foods, maxUnits):
  print("Use greedy by value to allocate", maxUnits, "calories")
  testGreedy(foods, maxUnits, Food.getValue)
  print("\nUse greedy by cost to allocate", maxUnits, "calories")
  testGreedy(foods, maxUnits, lambda x: 1 / Food.getCost(x))
  print("\nUse greedy by density to allocate", maxUnits, "calories")
  testGreedy(foods, maxUnits, Food.density)

testGreedys(800)

# Lambda - used to create anonymous functions, which don't have names
#            It's basically an expression, and the value of the expression is
#            the function. We use it by writing lambda followed by a list of 
#            arguments, and then an expression using those arguments.
#            It returns a function returning n arguments.

f1 = lambda x: x #Assign variable f1 to the lambda x:x or the identity function
f1(3) #Calls the lambda function with argument of 3
f1("reday") #Works with a string as well

# More complex lamda function:
f2 = lambda x, y: x + y #Assigns variable f2 to the given lamda function
f2(2, 3) #Calls the lambda function above with 2 as x and 3 as y
f2("reday", " zarra") #Works with adding strings as well

# Even MORE complex lambda function
f3 = lambda x, y: "factor" if (x % y == 0) else "not factor" #If-else expression
f3(4, 2) #Returns factor because 2 is a factor of 4
f3(4, 3) #Returns not a factor

# DON'T USE LAMBDA FUNCTIONS!!! Use def instead because lambdas can become complex
# Using greedy with variables assigned:
names = ["wine", "beer", "pizza", "burger", "fries", "cola", "apple", 
         "donut", "cake"]
values = [89, 95, 100, 90, 79, 50, 10]
calories = [123, 154, 258, 354, 365, 150, 95, 195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 750)

#Why does Greedy algorithms return different answers?
#            A sequence of locally "optimal" choices don't always return the
#            universally correct solution. 