import fileinput
import math

lines = list(line.strip() for line in fileinput.input())
time = int(lines[0])

bus_ids = [int(x) for x in lines[1].split(",") if x != "x"]
bus_ids_all = [x for x in lines[1].split(",")]


def find_earliest():
    delay = 0
    while True:
        for bus_id in bus_ids:
            if (time + delay) % bus_id == 0:
                return delay * bus_id
        delay += 1


def find_earliest_seq():
    bus_index_pairs = [(bus_id, bus_ids_all.index(str(bus_id))) for bus_id in bus_ids]
    cur_time = 1
    increment = 1
    for ii in range(2, len(bus_ids) + 1):
        working_buses = bus_index_pairs[:ii]
        print (working_buses)
        prev_match = 0
        while  True:
            for bus_id, offset in working_buses:
                if (cur_time + offset) % bus_id != 0:
                    cur_time += increment
                    break
            else:
                if prev_match == 0:
                    prev_match = cur_time
                    if ii == len(bus_ids):
                        break
                    cur_time += increment
                else:
                    increment = cur_time - prev_match
                    print (cur_time, increment)
                    break

    return cur_time

print ("part_1", find_earliest())
print ("part_2", find_earliest_seq())
