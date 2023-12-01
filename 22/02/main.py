draw = 'draw'
win = 'win'
lose = 'lose'
rock = 'rock'
paper = 'paper'
scissors = 'scissors'


def round_outcome_for_me(rps_combination: str):
    """
    Returns the outcome of the rock paper scissors game from the perspective of the non elf player.

    opponent signs:
        A: rock
        B: paper
        C: scissors
    player signs:
        X: rock
        Y: paper
        Z: scissors

    :param rps_combination: a combination of rock paper scissors symbols as described above
    :return: round outcome: draw/lose/win
    """

    possible_outcomes = {'AX': draw,
                         'AY': win,
                         'AZ': lose,
                         'BX': lose,
                         'BY': draw,
                         'BZ': win,
                         'CX': win,
                         'CY': lose,
                         'CZ': draw}

    outcome_score = {lose: 0, draw: 3, win: 6}

    return outcome_score[possible_outcomes[rps_combination]]


def predict_score(input_file_path: str):
    choice_score = {'X': 1, 'Y': 2, 'Z': 3}
    total_score = 0

    with open(input_file_path) as file:
        for line in file:
            this_rounds_score = round_outcome_for_me(line.replace(' ', '').strip()) + choice_score[line[2]]
            total_score += this_rounds_score

            print(f"Play this round: {line}")
            print(f"My score: {this_rounds_score}")
            print(f"Total score: {total_score}")
            print("\n =================== \n")

    print(f"Final score: {total_score}")

    return total_score


def symbol_choice(choice_and_outcome):
    correct_sign = { 'AX': scissors,
                     'AY': rock,
                     'AZ': paper,
                     'BX': rock,
                     'BY': paper,
                     'BZ': scissors,
                     'CX': paper,
                     'CY': scissors,
                     'CZ': rock}

    return correct_sign[choice_and_outcome]


def predict_score_from_outcomes(input_file_path: str):
    choice_score = {rock: 1, paper: 2, scissors: 3}
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
    total_score = 0

    with open(input_file_path) as file:
        for line in file:
            this_rounds_score = outcome_score[line[2]] + choice_score[symbol_choice(line.strip().replace(' ', ''))]
            total_score += this_rounds_score

            print(f"desired symbol")
            print(f"Play this round: {line}")
            print(f"My score: {this_rounds_score}")
            print(f"Total score: {total_score}")
            print("\n =================== \n")

    print(f"Final score: {total_score}")

    return total_score