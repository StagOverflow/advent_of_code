# Rules

# 1. The head (H) and tail (T) must always be touching
# (diagonally adjacent and even overlapping both count as touching):
#
# 2. If the head is ever two steps directly up, down, left, or right from the tail,
# the tail must also move one step in that direction so it remains close enough:
#
# 3. Otherwise, if the head and tail aren't touching and aren't
# in the same row or column, the tail always moves one step diagonally to keep up:

from enum import Enum
import math

class Direction(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


class HeadInput:
    def __init__(self, command: str):
        self.direction = Direction(command[0])
        self.steps = range(int(command[2]))


def move_head(head_position, direction: Direction):
    if direction == Direction.UP:
        return head_position[0] - 1, head_position[1]

    elif direction == Direction.DOWN:
        return head_position[0] + 1, head_position[1]

    elif direction == Direction.LEFT:
        return head_position[0], head_position[1] - 1

    elif direction == Direction.RIGHT:
        return head_position[0], head_position[1] + 1

    else:
        raise(Exception("Invalid direction input"))


def _add_tuples(tuple_a: tuple, tuple_b: tuple):
    return tuple(map(lambda x, y: x + y, tuple_a, tuple_b))


def move_tail(tail_position, head_position):
    def _move_lateral(tail, head):
        motion = head[1] - tail[1]
        return 0, motion - int(math.copysign(1, motion))  # The tail isn't moving the whole way to the head

    def _move_vertical(tail, head):
        motion = head[0] - tail[0]
        return motion - int(math.copysign(1, motion)), 0

    def _move_diagonal(tail, head):
        vertical_direction = head[0] - tail[0]
        lateral_direction = head[1] - tail[1]

        if vertical_direction >= 2:
            vertical_direction -= 1
        elif vertical_direction <= -2:
            vertical_direction += 1
        elif lateral_direction >= 2:
            lateral_direction -= 1
        else:
            lateral_direction += 1

        return vertical_direction, lateral_direction

    if tail_position == head_position:
        return tail_position
    elif tail_position[0] == head_position[0]:
        delta = _move_lateral(tail_position, head_position)
    elif tail_position[1] == head_position[1]:
        delta = _move_vertical(tail_position, head_position)
    else:  # The tail is moving in diagonal
        delta = _move_diagonal(tail_position, head_position)

    return _add_tuples(tail_position, delta)


def head_tail_contact(tail_position, head_position):
    """
    Are head and tail touching

    :param head_position:
    :param tail_position:
    :return: Whether they are touching or not: boolean
    """

    def _absolute_sub_tuples(tuple_a: tuple, tuple_b: tuple):
        return tuple(map(lambda x, y: abs(x - y), tuple_a, tuple_b))

    head_to_tail_delta = _absolute_sub_tuples(head_position, tail_position)

    return head_to_tail_delta in [(1, 0), (0, 1), (1, 1), (0, 0)]


def print_grid(head_position, tail_position, grid_size=30):

    grid = [[0]*grid_size]*grid_size

    for row_index in range(len(grid)):
        row = f'{row_index-grid_size//2} '
        if row[0] != '-':
            row += ' '
        for col in range(len(grid[row_index])):
            if (row_index, col) == tuple(map(lambda x: x + grid_size//2, head_position)):
                row = row + ' H '
            elif (row_index, col) == tuple(map(lambda x: x + grid_size//2, tail_position)):
                row = row + ' T '
            else:
                row = row + ' . '
        print(row)
    print('\n====================\n')


def track_tail_motion(input_path, grid_size=100, verbose=False):
    head_position = (0, 0)
    tail_position = (0, 0)
    tail_tracker = []
    head_tracker = []

    with open(input_path) as instructions:
        for line in instructions:
            motions = HeadInput(line.strip())
            for _ in motions.steps:
                head_position = move_head(head_position, motions.direction)

                if not head_tail_contact(tail_position, head_position):
                    tail_position = move_tail(tail_position, head_position)

                head_tracker.append(head_position)
                tail_tracker.append(tail_position)
    return tail_tracker, head_tracker


tail_tracker, head_tracker = track_tail_motion('sample.txt')

print(f"Head moves: {head_tracker}")
print(f"Tail moves: {tail_tracker}")
print(f"Number of unique spots: {len(set(tail_tracker))}")
