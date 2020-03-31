# Once upon a time, on a way through the old wild mountainous west,…
# … a man was given directions to go from one point to another. The directions were
# "NORTH", "SOUTH", "WEST", "EAST". Clearly "NORTH" and "SOUTH" are opposite, "WEST"
# and "EAST" too.

# Going to one direction and coming back the opposite direction right away is a needless
# effort. Since this is the wild west, with dreadfull weather and not much water,
# it's important to save yourself some energy, otherwise you might die of thirst!

# Task
# Write a function dirReduc which will take an array of strings and returns an array of
# strings with the needless directions removed (W<->E or S<->N side by side).


def dirReduc(arr):
    pairs = {0: ['NORTH', 'SOUTH'], 1: ['EAST', 'WEST']}
    i = 0
    while i < len(arr):
        try:
        # 'try' 'except' prevents the code from breaking when it looks for an element 
        # beyond the last index
            for each in pairs.values():
                current = each
                # setting each value to a variable allows me to reset the 'for' 
                # loop iterating over the values
                while arr[i] in current and arr[i + 1] in current:
                    # the above line makes sure the following direction is in the
                    # opposite direction
                    if arr[i] != arr[i + 1]:
                        # the man should be able to go in the same direction twice
                        arr.remove(arr[i + 1])
                        # removing the target index first would reset the value at both
                        # indeces
                        arr.remove(arr[i])
                        # here's where I reset both loops so that all conditions are
                        # checked for every element
                    i = 0
                    current = pairs[0]
        except IndexError:
            break
        i += 1
    return arr


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "WEST"])) 
