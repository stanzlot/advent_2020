import fileinput
import re
import math

lines_b = [[entry for entry in grp.split("\n")]\
            for grp in "".join(fileinput.input()).split("\n\n")]

rules = [re.match("([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", rule_line).groups()\
          for rule_line in lines_b[0]]
rules = dict([(rule_grp[0], ((range(int(rule_grp[1]), int(rule_grp[2])+ 1),\
                            range(int(rule_grp[3]), int(rule_grp[4]) + 1))))\
             for rule_grp in rules])
your_tickets = [int(x) for x in "".join(lines_b[1][1:]).split(",")]
near_by_tickets = [[int(x) for x in "".join(tick_line).split(",") if x.isdigit()] \
                   for tick_line in lines_b[2][1:] if tick_line != ""]
valid_near_by = []
invalid_sum = 0
for ticket in near_by_tickets:
    is_valid_ticket = True
    for field in ticket:
        if not any ([field in lower or field in upper \
                     for field_name, (lower, upper) in rules.items()]):
            invalid_sum += field
            is_valid_ticket = False
    if is_valid_ticket:
        valid_near_by.append(ticket)

field_id_by_type = {}
for ticket in valid_near_by:
    for ii in range(len(ticket)):
        field = ticket[ii]
        for field_name, (lower, upper) in rules.items():
            if field in lower or field in upper:
                if not ii in field_id_by_type:
                    field_id_by_type[ii] = {}

                if not field_name in field_id_by_type[ii]:
                    field_id_by_type[ii][field_name] = 1
                else:
                    field_id_by_type[ii][field_name] += 1

id_by_pos = []
for field_id, field_valid_count in field_id_by_type.items():
    pos_field = 0
    for field_name, num_valid in field_valid_count.items():
        if num_valid == len(valid_near_by):
            pos_field +=1
    id_by_pos.append((pos_field, field_id))

id_by_pos.sort()

field_decode = {}
for pos_matches, field_id in id_by_pos:
    field_valid_count = field_id_by_type[field_id]
    for field_name, num_valid in field_valid_count.items():
        if num_valid == len(valid_near_by)\
            and field_name not in field_decode:
            field_decode[field_name] = field_id
            break


print ("part_1", invalid_sum)
print("part_2", math.prod([your_tickets[field_id]\
    for field_name, field_id  in field_decode.items() \
        if field_name.startswith("depart")]))

