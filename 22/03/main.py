# The list of items for each rucksack is given as characters all on a single line.
# A given rucksack always has the same number of items in each of its two compartments,
# so the first half of the characters represent items
# in the first compartment, while the second half of the characters represent items in the second compartment.


def item_priority(item: str) -> int:
    if item.isupper():
        return ord(item) - 38  # a -> z : 97 -> 122
    else:
        return ord(item) - 96  # A -> z : 65 -> 90


def rucksack_compartment_to_dict(rucksack: str):
    first_compartment = {}
    for item in rucksack:
        if item not in first_compartment.keys():
            first_compartment[item] = 0
    return first_compartment


def split_rucksack(rucksack: str):
    half = len(rucksack) // 2
    first_comp, second_comp = rucksack[:half], rucksack[half:]
    return first_comp, second_comp


def check_for_dupes(compt_one: dict, compt_two: str) -> set:
    dupes = set()
    for item in compt_two:
        if item in compt_one:  # Using a dict like a set because I am suspecting we'll be counting stuff next round :)
            dupes.add(item)
    return dupes


def check_rucksack_valid(input_file_path: str) -> int:
    with open(input_file_path) as file:
        total_score = 0
        for rucksack in file:
            first_half, second_half = split_rucksack(rucksack.strip())
            first_half_dict = rucksack_compartment_to_dict(first_half)
            duplicates = check_for_dupes(first_half_dict, second_half)
            rucksack_dupe_score = sum([item_priority(dupe) for dupe in duplicates])
            total_score += rucksack_dupe_score

    return total_score


# Part two
def find_groups_badge(input_file_path: str) -> int:
    with open(input_file_path) as file:
        total_score = 0
        group_counter = 0
        for rucksack in file:
            if group_counter == 0:  # first elf, anything is on the table
                common_items = {i: 1 for i in rucksack.strip()}
            else:
                item_types = set(rucksack)
                for item in item_types:
                    if item in common_items:
                        common_items[item] += 1

            if group_counter == 2:
                score = item_priority([item for item in common_items if common_items[item] == 3][0])
                total_score += score
                group_counter = 0
                common_items = {}
            else:
                group_counter += 1

    return total_score




