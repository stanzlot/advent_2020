import fileinput
import copy

seat_grid = [list(x.strip()) for x in fileinput.input()]

def print_grid(seat_grid):
    print("\n")
    for row in seat_grid:
        print("".join(row))
    print("\n")

adjacent_offset = {
    "left" : (0, -1),
    "right" : (0, 1),
    "up" : (-1, 0),
    "down" : (1, 0),
    "left_up" : (-1, -1),
    "right_up" : (-1, 1),
    "left_down" : (1, -1),
    "right_down" : (1, 1),
}

def is_seat_loc(seat_grid, dX, dY):
    return 0 <= dX < len(seat_grid[0]) and 0 <= dY < len(seat_grid)

def process_seat_grid(seat_grid, occup_limit):
    prev_grid = copy.deepcopy(seat_grid)
    has_changed = False
    for yy in range(len(seat_grid)):
        for xx in range(len(seat_grid[yy])):
            seat_val = prev_grid[yy][xx]
            occupied_adjacent = 0
            for dX, dY in adjacent_offset.values():
                adjX = xx + dX
                adjY = yy + dY
                while is_seat_loc(seat_grid, adjX, adjY) and\
                      prev_grid[adjY][adjX] == "." and occup_limit > 4:
                    adjX += dX
                    adjY += dY
                if not is_seat_loc(seat_grid, adjX, adjY) :
                    continue
                if prev_grid[adjY][adjX] == "#":
                    occupied_adjacent += 1
            if seat_val == "L" and occupied_adjacent == 0:
                seat_grid[yy][xx] = "#"
                has_changed = True
            elif seat_val == "#" and occupied_adjacent >= occup_limit:
                seat_grid[yy][xx] = "L"
                has_changed = True
    return has_changed

seat_grid_orig = copy.deepcopy(seat_grid)
while process_seat_grid(seat_grid, 4):
    pass
print ("part_1", sum([row.count("#") for row in seat_grid]))

seat_grid = seat_grid_orig
while process_seat_grid(seat_grid, 5):
    pass
print ("part_2", sum([row.count("#") for row in seat_grid]))
