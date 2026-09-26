# This program initializes a tuple of strings representing different emotions
# And uses a conditional expression to print "true" if the last element is "happy" and there are more than 3 elements, 
# or “false” if it is not.

# Name: Ava Puaatuua
# Date: Sept. 25, 2026

emotions = ("surprise", "sad", "fear", "happy", "anxious")

result = emotions[-1] == "happy" and len(emotions) > 3
print(result)

# len(emotions) counts how many elements are in the emotions tuple
# len(emotions > 3) = 4 > 3, so the second part of the conditional expression is true
# the first condition is emotions[-1] == "happy", which is false because the last element is "surprise"
# because the conditions are joined with and, both must be true

# Using an if statement
if emotions[-1] == "happy" and len(emotions) > 3:
    print("true")
else:
    print("false")