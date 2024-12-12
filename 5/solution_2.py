with open("5/input.txt", "r") as f:
    content = f.read()

    orderings, updates = content.split("\n\n")

    ordering_list = orderings.split("\n")
    
    # Remove empty strings
    updates_list = list(filter(None, updates.split("\n")))

    for i in range(len(updates_list)):
        updates_list[i] = [int(num) for num in updates_list[i].split(',')]

    order_rules = {}
    
    for line in ordering_list:
        before, after = line.split("|")
        
        before = int(before)
        after = int(after)

        if before not in order_rules.keys():
            order_rules[before] = [after]
        else:
            order_rules[before].append(after)

# Find invalid updates
invalid_updates_list = []
for update in updates_list:

    for i in range(1, len(update)):

        if update[i] in order_rules.keys():

            if any(after in update[:i] for after in order_rules[update[i]]):
                invalid_updates_list.append(update)
                break

corrected_update_middle_sum = 0

for update in invalid_updates_list:

    changed = True

    while changed:

        changed = False

        for i in range(1, len(update)):

            if update[i] in order_rules.keys():

                for j in range(len(update[:i])):

                    if update[j] in order_rules[update[i]]:

                        tmp = update[i]
                        del update[i]
                        update = update[:j] + [tmp] + update[j:]
                        changed = True
                        break
            
            if changed:
                break
    
    corrected_update_middle_sum += update[len(update)//2]


print(corrected_update_middle_sum)
        
        
