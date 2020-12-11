import fileinput
import itertools

msg_encoded = list(map(int,fileinput.input()))

def find_invalid():
    offset = 25
    for ii in range(offset, len(msg_encoded)):
        preamble_pairs = itertools.combinations(msg_encoded[ii - offset : ii], 2)
        if not any([msg_encoded[ii] == sum(num_pair) for num_pair in preamble_pairs]):
            return msg_encoded[ii]

def find_match_seq(target_num):
    for ii in range(2, len(msg_encoded) - 1):
        for jj in range(len(msg_encoded) - ii):
            seq_match = msg_encoded[jj : jj + ii]
            if target_num == sum(seq_match):
                return min(seq_match) + max(seq_match)

print("part_1", find_invalid())
print("part_2", find_match_seq(find_invalid()))

