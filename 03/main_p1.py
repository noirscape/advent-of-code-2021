# Generic functions

def read_file_into_list(filename):
    """Reads a file into a list of strings"""
    with open(filename, "r") as filehandle:
        lst = filehandle.read().splitlines()
    return lst

def convert_list_to_object(lst, object):
    """Quickly convert all the items in a list to the object/class passed in"""
    return [object(x) for x in lst]

# Goal: calculate most and least common bit position, then convert to decimal.
data = read_file_into_list("input.txt")

outcome_g = []
outcome_e = []
for idx, _ in enumerate(data[0]): # iterate over one length of the list
    zero_freq = 0
    one_freq = 0
    for d in data:
        if d[idx] == "0":
            zero_freq += 1
        else:
            one_freq += 1
    if zero_freq > one_freq:
        outcome_g.append("0")
        outcome_e.append("1")
    else:
        outcome_g.append("1")
        outcome_e.append("0")

outcome_g = "".join(outcome_g)
outcome_e = "".join(outcome_e)

print(f"Gamma rate: {outcome_g} [binary] / {int(outcome_g, 2)} [decimal]")
print(f"Epsilon rate: {outcome_e} [binary] / {int(outcome_e, 2)} [decimal]")
print(f"Consumption rate (solution): {int(outcome_g, 2) * int(outcome_e, 2)}")