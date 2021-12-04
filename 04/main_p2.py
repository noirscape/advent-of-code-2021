# useful imports
from pprint import pprint
# Generic functions

def read_file_into_list(filename):
    """Reads a file into a list of strings"""
    with open(filename, "r") as filehandle:
        lst = filehandle.read().splitlines()
    return lst

def convert_list_to_object(lst, object):
    """Quickly convert all the items in a list to the object/class passed in"""
    return [object(x) for x in lst]

class BingoBoard:
    """Class to store a bingo board in. Accepts lines which it converts to a 2-dimensional array."""
    def __init__(self, lines) -> None:
        self.board_layout = []
        self.marked_layout = []
        for line in lines:
            row = convert_list_to_object(line.split(), int)
            mark_row = [False for _ in row]
            self.board_layout.append(row)
            self.marked_layout.append(mark_row)

        self.winner = False 

    def mark_number(self, number):
        for x, line in enumerate(self.board_layout):
            for y, value in enumerate(line):
                if number == value:
                    self.marked_layout[x][y] = True

    def winner_check(self):
        # win check: vertical full and horizontal full. this function also sets the winner attribute to True

        # we start with horizontal check
        for line in self.marked_layout:
            if all(line): # all checks if every value is true!
                self.winner = True
                return True
        
        # ok not horizontal win, how about vertical next
        for vidx in range(len(self.marked_layout[0])):
            vertical_line = []
            for line in self.marked_layout: # iterate over line, append each slice item to the list
                vertical_line.append(line[vidx])
            if all(vertical_line): # then check if vertical line is true
                self.winner = True
                return True
        
        return False # if false, nobody wins

    def calculate_score(self, last_call):
        # step 1: sum up every unmarked number
        unmarked_sum = 0
        for x, line in enumerate(self.board_layout):
            for y, value in enumerate(line):
                if self.marked_layout[x][y] == False:
                    unmarked_sum += value

        # step 2: multiply every unmarked number by the last call and return that
        return unmarked_sum * last_call

# Goal: calculate last winning board
data = read_file_into_list("input.txt")

# step 1: convert the first line into a list of numbers to draw
draw_order = convert_list_to_object(data[0].split(","), int)
print(draw_order)

# step 2: parse the rest of the file into bingo boards
boards = []
for idx, line in enumerate(data):
    if idx == 0: # already parsed this
        continue
    elif line == "": # empty line = new board
        boards.append(BingoBoard(data[idx+1:idx+6])) # idx + 1 / idx + 6, the currentl ine does not need parsing


print(f"Considering {len(boards)} boards.")

# step 3: start drawing numbers until victor
last_call = -1
last_winner = None
for draw in draw_order:
    for board in boards:
        board.mark_number(draw)
        if board.winner_check():
            if all([b.winner for b in boards]):
                last_winner = board
                last_call = draw
                break
    if last_winner:
        break

# step 4: calculate winner score
print(f"The last board score is: {last_winner.calculate_score(last_call)}")
