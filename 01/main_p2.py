# Generic functions

def read_file_into_list(filename):
    """Reads a file into a list of strings"""
    with open(filename, "r") as filehandle:
        lst = filehandle.read().splitlines()
    return lst

def convert_list_to_object(lst, object):
    """Quickly convert all the items in a list to the object/class passed in"""
    return [object(x) for x in lst]

# Goal: figure out the amount of increases in a three-value measurement window

# first we get our input data
data = convert_list_to_object(read_file_into_list("input.txt"), int)

# then we start iterating
global_counter = 0
check_value = 0
sliding_windows = []

# first we iterate to make the sliding windows
for idx, d in enumerate(data):
    # before continuing, check if there is enough left in the list to make a sliding window
    if idx + 3 > len(data):
        # if there's not, then we quit early
        break
    else:
        sliding_windows.append(sum([data[idx], data[idx+1], data[idx+2]]))

for idx, d in enumerate(sliding_windows):
    if idx == 0: # index 0 is a special case
        check_value = d
        print(f"{idx+1} - {d} (N/A - no previous sum)")
        continue
    else:
        if d > check_value:
            print(f"{idx+1} - {d} (increased)")
            global_counter += 1
        else:
            print(f"{idx+1} - {d} (decreased)")
        check_value = d

print(f"\nSliding windows - {len(sliding_windows)}")
print(f"\nSliding window increases - {global_counter}")