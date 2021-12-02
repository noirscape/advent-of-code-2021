# Generic functions

def read_file_into_list(filename):
    """Reads a file into a list of strings"""
    with open(filename, "r") as filehandle:
        lst = filehandle.read().splitlines()
    return lst

def convert_list_to_object(lst, object):
    """Quickly convert all the items in a list to the object/class passed in"""
    return [object(x) for x in lst]

# Goal: calculate final x/y position based on instructions, then * them together

# minimal wrapper class to hold for generic function
class PositionChange:
    def __init__(self, string):
        split_string = string.split()
        self.movement = split_string[0]
        self.position = int(split_string[1])

data = convert_list_to_object(read_file_into_list("input.txt"), PositionChange)

x_pos = 0 # horizontal
y_pos = 0 # vertical
for d in data:
    if d.movement == "forward":
        x_pos += d.position
    elif d.movement == "down":
        y_pos += d.position
    elif d.movement == "up":
        y_pos -= d.position

    print(f"{d.movement} - {d.position} [{x_pos}, {y_pos}]")

print(f"The final position is [{x_pos}, {y_pos}]. Puzzle answer is {x_pos*y_pos}.")
