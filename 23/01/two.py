DIGITS = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def parse_digit(s):
    return


def contains_digit(b):
    # This is a cheap trick... Ideally we would check as we go and reset the buffer accordingly
    for digit in DIGITS.keys():
        if digit in b:
            return DIGITS[digit]
    return None


def calibration_sum(input_path='input.csv'):
    with open(input_path) as file:
        result = 0

        for line in file:
            num_first = None
            num_last = None
            buffer = ""

            for c in line:
                is_numeric = c.isnumeric()

                if not num_first and is_numeric:
                    num_first = num_last = int(c)
                elif is_numeric:
                    num_last = int(c)

                if not is_numeric and c != '\n':
                    buffer += c
                else:
                    buffer = ""

                buffer_digit = contains_digit(buffer)

                if buffer_digit:
                    if not num_first:
                        num_first = num_last = buffer_digit
                    else:
                        num_last = buffer_digit
                    buffer = ""

            if not num_first:
                raise ValueError("The line did not any numbers")

            result += 10 * num_first + num_last

    return result


print(calibration_sum())
