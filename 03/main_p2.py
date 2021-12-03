# Generic functions

def read_file_into_list(filename):
    """Reads a file into a list of strings"""
    with open(filename, "r") as filehandle:
        lst = filehandle.read().splitlines()
    return lst

def convert_list_to_object(lst, object):
    """Quickly convert all the items in a list to the object/class passed in"""
    return [object(x) for x in lst]

# Goal: reduce an input set down to the most/least common bit in each list
data = read_file_into_list("input.txt")

outcome_g = []
outcome_e = []

reduced_data_oxygen = []
reduced_data_scrubber = []

def iterate_over_data(data, pos, most_common):
    # steps:
    # 1: determine list frequency of bit start_pos (x starts at 0)
    zero_freq = 0
    one_freq = 0
    for d in data:
        if d[pos] == "0":
            zero_freq += 1
        else:
            one_freq += 1
    # 2: generate new list based on more frequent number
    new_data = []
    if most_common:
        if one_freq > zero_freq or one_freq == zero_freq: # one_freq is more common or equal
            for d in data:
                if d[pos] == "1":
                    new_data.append(d)
        else: # zero_freq is more common
            for d in data:
                if d[pos] == "0":
                    new_data.append(d)
    else:
        if zero_freq > one_freq: # one_freq is less common
            for d in data:
                if d[pos] == "1":
                    new_data.append(d)
        else: # zero_freq is less common or equal
            for d in data:
                if d[pos] == "0":
                    new_data.append(d)

    # 3: do it again until one remains
    if len(new_data) == 1:
        return new_data[0]
    else:
        return iterate_over_data(new_data, pos + 1, most_common)

reduced_data_oxygen = iterate_over_data(data, 0, True)
reduced_data_scrubber = iterate_over_data(data, 0, False)

print(f"Oxygen generator rating: {reduced_data_oxygen} [binary] / {int(reduced_data_oxygen, 2)} [decimal]")
print(f"CO2 scrubber rating: {reduced_data_scrubber} [binary] / {int(reduced_data_scrubber, 2)} [decimal]")
print(f"Life support rating (solution): {int(reduced_data_oxygen, 2) * int(reduced_data_scrubber, 2)}")