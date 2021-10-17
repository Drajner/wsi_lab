

def backpack(max_weight, items_weight, items_worth):

    items_in_backpack = []
    best_outcome = 0
    best_outcome_value = 0
    max_binary = 0b1 * (2**(len(items_weight))) - 1
    
    while max_binary >= 0:
        current_weight = 0
        current_value = 0
        for item in items_weight:
            if ((max_binary >> items_weight.index(item)) % 2) == 1:
                current_weight += item
                current_value += items_worth[items_weight.index(item)]
        if current_weight <= max_weight:
            if current_value > best_outcome_value:
                best_outcome_value = current_value
                best_outcome = max_binary
        max_binary -= 1
    
    for item in items_weight:
            if (best_outcome >> items_weight.index(item)) % 2:
                items_in_backpack.append([item, items_worth[items_weight.index(item)]])

    return items_in_backpack


def backpackPW(max_weight, items_weight, items_worth):

    items_in_backpack_weight = 0
    items_in_backpack = []

    while items_in_backpack_weight <= max_weight:

        max_p_w = 0
        max_p_w_item = 0
        for i in range(len(items_weight)):

            if((items_worth[i] / items_weight[i]) > max_p_w):
                max_p_w = items_worth[i] / items_weight[i]
                max_p_w_item = i

        if(items_in_backpack_weight + items_weight[max_p_w_item] <= max_weight):
            new_item = [items_weight[max_p_w_item], items_worth[max_p_w_item]]
            items_in_backpack.append(new_item)
            items_in_backpack_weight += items_weight[max_p_w_item]
            items_weight.remove(items_weight[max_p_w_item])
            items_worth.remove(items_worth[max_p_w_item])

        else:
            break

    return items_in_backpack


print(backpack(9, [8, 3, 5, 2], [16, 8, 9, 6]))

print(backpackPW(9, [8, 3, 5, 2], [16, 8, 9, 6]))
