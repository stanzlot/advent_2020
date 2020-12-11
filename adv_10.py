import fileinput

amps = sorted(list(map(int, fileinput.input())))
amps.append(amps[-1] + 3)
amps.insert(0, 0)

ams_next_pairs = list(zip(amps, amps[1:]))

deltas = [next_val - cur_val for cur_val, next_val in ams_next_pairs]
print ("part_1", deltas.count(3) * deltas.count(1))

def find_num_path(amps, index, cache_vals):
    if index == len(amps) - 1:
        return 1
    if index in cache_vals:
        return cache_vals[index]
    paths = 0
    for jj in range(min(3, len(amps) - index - 1)):
        if amps[index + jj + 1] - amps[index]  <= 3:
            paths += find_num_path(amps, index + jj + 1, cache_vals)
        else:
            break
    cache_vals[index] = paths
    return paths;

print ("part_2", find_num_path(amps, 0, {}))
