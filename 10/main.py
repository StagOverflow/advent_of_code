# 2 cycles to add to x
# signal strength = cycle number * x


def signal_strength(input_path, cycles_of_interest):
    cycle_counter = 1
    x = 1
    add_queue = []
    result = 0

    with open(input_path) as commands:

        line = commands.readline().strip()

        while line or add_queue:
            if add_queue:
                x += add_queue.pop()
            else:
                instruction = line.split(' ')

                if instruction[0] == 'addx':
                    add_queue.insert(0, int(instruction[1]))

                line = commands.readline().strip()

            if cycle_counter in cycles_of_interest:
                result += x * cycle_counter

            cycle_counter += 1

    return result



print(signal_strength('sample.txt', [20, 60, 100, 140, 180, 220]))