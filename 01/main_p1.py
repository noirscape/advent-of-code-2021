# Generic functions

def read_file_into_list(filename):
    """Reads a file into a list of strings"""
    with open(filename, "r") as filehandle:
        lst = filehandle.read().splitlines()
    return lst

def convert_list_to_object(lst, object):
    """Quickly convert all the items in a list to the object/class passed in"""
    return [object(x) for x in lst]

# Goal: figure out the amount of increases in a single number of code and print out the result.

# first we get our input data
data = convert_list_to_object(read_file_into_list("input.txt"), int)

# then we start iterating
global_counter = 0
check_value = 0

for idx, d in enumerate(data):
    if idx == 0: # index 0 is a special case
        check_value = d
        print(f"{d} (N/A - no previous measurement)")
        continue
    else:
        if d > check_value:
            print(f"{d} (increased)")
            global_counter += 1
        else:
            print(f"{d} (decreased)")
        check_value = d

print(f"\nTotal increases - {global_counter}")