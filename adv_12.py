import fileinput
import re

navigations = [(line[0], int(line[1:])) for line in fileinput.input()]

directions = {
    "N" : (0, -1),
    "S" : (0, 1),
    "E" : (1, 0),
    "W" : (-1, 0)
}

right_turn = {
    "N" : "E",
    "S" : "W",
    "E" : "S",
    "W" : "N"
}

def process_direct_nav():
    orient = "E"
    xx = yy = 0
    for inst_name, inst_value in navigations:
        if inst_name in directions:
            dX, dY = directions[inst_name]
            xx += inst_value * dX
            yy += inst_value * dY
        elif inst_name in ["L","R"]:
            for ii in range(inst_value // 90 * (1 if inst_name == "R" else 3)):
                orient = right_turn[orient]
        else:
            dX, dY = directions[orient]
            xx += inst_value * dX
            yy += inst_value * dY
    return abs(xx) + abs(yy)

def process_waypoint_nav():
    xx = yy = 0
    waypoint = (10, -1)
    for inst_name, inst_value in navigations:
        if "F" == inst_name:
            xx += waypoint[0] * inst_value
            yy += waypoint[1] * inst_value
        elif inst_name in directions:
            dX, dY = directions[inst_name]
            waypoint = (waypoint[0] + dX * inst_value, waypoint[1] + dY * inst_value)
        elif inst_name in ["L", "R"]:
            for ii in range(inst_value // 90 * (1 if inst_name == "R" else 3)):
                waypoint = (-1 * waypoint[1], 1 * waypoint[0])
    return abs(xx) + abs(yy)

print("part_1", process_direct_nav())
print("part_2", process_waypoint_nav())
