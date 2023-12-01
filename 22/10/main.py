def signal_strength(input_path, cycles_of_interest):
    cycle_counter = 1
    line_counter = 1
    x = 1
    result = 0

    add_queue = []
    history = []

    with open(input_path) as commands:
        line = commands.readline().strip()

        while line or add_queue:
            if cycle_counter in cycles_of_interest:
                result += x * cycle_counter

            if add_queue:
                x += add_queue.pop()
            else:
                instruction = line.split(' ')

                if instruction[0] == 'addx':
                    add_queue.insert(0, int(instruction[1]))

                line = commands.readline().strip()
                history.append(instruction)
                line_counter += 1


            cycle_counter += 1
    return result


def render_sprite(input_path):
    cycle_counter = 1
    line_counter = 1
    x = 1
    add_queue = []

    rendered_line = ''

    with open(input_path) as commands:

        line = commands.readline().strip()

        while line or add_queue:
            horizontal_pixel = (cycle_counter - 1) % 40
            if horizontal_pixel in (x-1, x, x+1):
                rendered_line += '#'
            else:
                rendered_line += '.'

            if cycle_counter % 40 == 0:
                print(rendered_line)
                rendered_line = ''

            if add_queue:
                x += add_queue.pop()
            else:
                instruction = line.split(' ')

                if instruction[0] == 'addx':
                    add_queue.insert(0, int(instruction[1]))

                line = commands.readline().strip()
                line_counter += 1

            cycle_counter += 1
    return


print(signal_strength('input.txt', [20, 60, 100, 140, 180, 220]))

render_sprite('input.txt')
