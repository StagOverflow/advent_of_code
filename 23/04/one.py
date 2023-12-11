import collections
import re

if __name__ == '__main__':
    rxp = re.compile(r'\b\d+\s*:\s*([^\|]+)\s+\|\s+([^\n]+)')

    with open('input.csv') as f:
        total = 0
        for line in f:
            match = re.search(rxp, line)
            target_nums = set(map(int, re.split(r'\s+', match.group(1).strip())))
            draw_nums = collections.Counter((map(int, re.split(r'\s+', match.group(2).strip()))))
            winnings = [draw_nums[e] for e in target_nums if e in draw_nums]
            if winnings:
                total += 2 ** (sum(winnings) - 1)

        print(total)

# 119535
