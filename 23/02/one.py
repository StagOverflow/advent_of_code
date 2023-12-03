"""
 * bag of cubes
 * cubes are red green or blue
 * goal is to find out how many cubes are in the bags

 * Q1: Which games would have been possible if the bag contains
 12 red cubes, 13 green cubes, 14 blue cubes

 * First thought:
    * Iterate through the games
        * if the current game has one impossible sample, tag it as impossible
        * else if we go through every sample for the game, add its ID to the sum
    * Possible edge cases:
        * one game with no valid sample
        * no valid game -> won't happen, undefined, could raise
        * assuming all sample numbers are integers


"""

# Note: Currently we only care about a single sample not following the rule
# so we can treat session splitting semi-colons and color splitting commas the same

# def parse_game():

import re


def day_2(input_path='input.csv'):
    cubes_available = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    result = 0

    with open(input_path) as file:
        for line in file:
            samples = re.compile(r'(\d+)\s(blue|green|red)').findall(line)
            is_valid = True
            for s in samples:
                if cubes_available[s[1]] < int(s[0]):
                    is_valid = False
                    break
            if is_valid:
                game_id = re.compile(r'^Game (\d+).*$')
                result += int(game_id.match(line).group(1))

    return result

print(day_2('input.csv'))
