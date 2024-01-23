#   Write a function named only_ints that takes two parameters. 
#   Function should return True if both parameters are integers, and False otherwise.

#E.g, calling only_ints(1,2) should return True, 
#while calling only_ints("a", 1) should return False.

def only_ints(one, two):
    return True if isinstance(one, int) and isinstance(two, int) else False

print(only_ints(1, 3)) # True
print(only_ints("a", 3)) # False