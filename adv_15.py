import fileinput

game_nums = [line.strip() for line in fileinput.input()]
game_nums = [int(x) for x in game_nums[0].split(",")]

def find_turn_num(seq_num):
    game_num_seq = dict((num, index + 1) for index, num in enumerate(game_nums))
    prev_turn = game_nums[-1]
    cur_turn = None
    for ii in range(len(game_nums) + 1, seq_num + 1):
        if prev_turn not in game_num_seq or game_num_seq[prev_turn] == ii - 1:
            cur_turn = 0
        else:
            cur_turn = ii - game_num_seq[prev_turn] - 1

        game_num_seq[prev_turn] = ii - 1
        prev_turn = cur_turn
    return cur_turn

print ("part_1", find_turn_num(2020))
print ("part_2", find_turn_num(30000000))

