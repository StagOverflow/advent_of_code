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


def move_tail(tail_position, head_position):
    # TODO: right the head and tail would overlap, really we want the tail to only move one tile
    # alternatively the tail could move to the spot of the head - 1 step in each direction, that
    # one step however needs to maintain the direction (+ or -) of the motion

    def _move_lateral(tail, head):
        motion = head[1] - tail[1]
        return 0, motion - int(math.copysign(1, motion))  # The tail isn't moving the whole way to the head

    def _move_vertical(tail, head):
        motion = head[0] - tail[0]
        return motion - int(math.copysign(1, motion)), 0

    def _add_tuples(tuple_a: tuple, tuple_b: tuple):
        return tuple(map(lambda x, y: x + y, tuple_a, tuple_b))

    def _move_diagonal(tail, head):
        return _add_tuples(_move_vertical(tail, head), _move_lateral(tail, head))

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


def track_tail_motion(input_path, grid_size=100):
    head_position = (0, 0)
    tail_position = (0, 0)
    tail_tracker = []
    head_tracker = []

    with open(input_path) as instructions:
        for line in instructions:
            motions = HeadInput(line.strip())
            for _ in motions.steps:
                head_position = move_head(head_position, motions.direction)
                head_tracker.append(head_position)
                if not head_tail_contact(tail_position, head_position):
                    tail_position = move_tail(tail_position, head_position)
                    tail_tracker.append(tail_position)

    return tail_tracker, head_tracker


tail_tracker, head_tracker = track_tail_motion('input.txt')

# print(f"Head moves: {head_tracker}")
# print(f"Tail moves: {tail_tracker}")
print(f"Number of unique spots: {len(set(tail_tracker))}")
