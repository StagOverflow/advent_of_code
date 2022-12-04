# Part one
def is_full_overlap(assignment1, assignment2):
    if (assignment1[0] >= assignment2[0] and assignment1[1] <= assignment2[1]) or (assignment2[0] >= assignment1[0] and assignment2[1] <= assignment1[1]):
        return True
    return False


def parse_pair(line: str):
    elves = list(map(lambda s: s.split('-'), line.split(',')))
    result = [list(map(lambda x: int(x), e)) for e in elves]
    return result


def count_fully_overlapping_pairs(input_file_path):
    overlapping_pairs = 0

    with open(input_file_path) as file:
        for line in file:
            elf1, elf2 = parse_pair(line.strip())
            if is_full_overlap(elf1, elf2):

                overlapping_pairs += 1

    return overlapping_pairs


# Part Two
def between(number: int, my_range: tuple) -> bool:
    if my_range[0] <= number <= my_range[1]:
        return True


def is_overlap(assignment1, assignment2):
    if between(assignment1[0], assignment2) or between(assignment2[0], assignment1) or between(assignment1[1], assignment2) or between(assignment2[1], assignment1):
        return True
    return False


def count_all_overlapping_pairs(input_file_path):
    overlapping_pairs = 0

    with open(input_file_path) as file:
        for line in file:
            elf1, elf2 = parse_pair(line.strip())
            if is_overlap(elf1, elf2):
                overlapping_pairs += 1

    return overlapping_pairs
