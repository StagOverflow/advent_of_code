def detect_start_of_sequence(input_path, n):
    last_four_chars = []
    counter = 0
    with open(input_path) as f:
        for line in f:
            for char in line:
                if len(last_four_chars) < n:
                    last_four_chars.insert(0, char)
                else:
                    if len(last_four_chars) == len(set(last_four_chars)):
                        return counter

                    last_four_chars.insert(0, char)
                    last_four_chars.pop()
                counter += 1
    return None


print(detect_start_of_sequence('input.csv', 4))
print(detect_start_of_sequence('input.csv', 14))

