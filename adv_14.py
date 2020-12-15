import fileinput
import re
# from bitstring import BitArray

lines = [line.strip() for line in fileinput.input()]

def process_mem_cmds():
    mask = None
    mask_zero_val = None
    mask_ones_val = None
    mem = {}
    for cmd in lines:
        if cmd.startswith("mask"):
            mask = re.split(" = ", cmd)[1]
            mask_zero_val = int(mask.replace("X", "0"), 2)
            mask_ones_val = int(mask.replace("X", "1"), 2)
        else:
            mem_addr, value = (re.match("^mem\[(\d+)\] = (\d+)$", cmd).groups())
            calc_val = (int(value) | mask_zero_val) & mask_ones_val
            mem[mem_addr] = calc_val
    return sum([x for x in mem.values()])

def process_mem_decode_cmds():
    mask = None
    mask_zero_val = None
    mem = {}
    for cmd in lines:
        if cmd.startswith("mask"):
            mask = re.split(" = ", cmd)[1]
            mask_zero_val = int(mask.replace("X", "0"), 2)
            continue

        mem_addr, value = (re.match("^mem\[(\d+)\] = (\d+)$", cmd).groups())
        floating_locs = [ii for ii in range(len(mask)) if mask[ii] == "X"]
        format_p = "{0:0"+ str(len(floating_locs)) + "b}"
        mem_addr_val = int(mem_addr) | mask_zero_val
        for ii in range(2 ** len(floating_locs)):
            float_template = format_p.format(ii)
            mask_float = list("{0:036b}".format(int(mem_addr_val)))
            for jj in range(len(float_template)):
                mask_float[floating_locs[jj]] = float_template[jj]
            mask_float_val = int("".join(mask_float), 2)
            mem[mask_float_val] = int(value)

    return sum([x for x in mem.values()])

print ("part_1", process_mem_cmds())
print ("part_2", process_mem_decode_cmds())
