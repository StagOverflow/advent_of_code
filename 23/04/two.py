import collections
import re

if __name__ == '__main__':
    rxp = re.compile(r'\b\d+\s*:\s*([^\|]+)\s+\|\s+([^\n]+)')

    with open('input.csv') as f:
        total = 0
        copies = {}

        for current_card, line in enumerate(f, start=1):
            if current_card in copies:
                copies[current_card] += 1
            else:
                copies[current_card] = 1

            match = re.search(rxp, line)
            target_nums = set(map(int, re.split(r'\s+', match.group(1).strip())))
            draw_nums = collections.Counter((map(int, re.split(r'\s+', match.group(2).strip()))))

            winning_numbers = sum([draw_nums[e] for e in target_nums if e in draw_nums])

            for n in range(current_card + 1, current_card + winning_numbers + 1):
                if n in copies:
                    copies[n] += copies[current_card]
                else:
                    copies[n] = copies[current_card]

            total += copies[current_card]
    print(total)
