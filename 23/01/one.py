def calibration_sum(input_path='input.csv'):
    with open(input_path) as file:
        result = 0

        for line in file:
            num_first = None
            num_last = None
            for c in line:
                is_numeric = c.isnumeric()

                if not num_first and is_numeric:
                    num_first = num_last = int(c)
                elif is_numeric:
                    num_last = int(c)

            if not num_first:
                raise ValueError("The line did not any numbers")

            result += 10 * num_first + num_last

    return result


print(calibration_sum())
