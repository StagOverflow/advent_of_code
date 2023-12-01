def hungry_elf(input_file_path):
    with open(input_file_path) as calorie_list:
        cur_elf_cals = 0
        max_elf_cals = 0
        elf_counter = 0

        for line in calorie_list:
            if not line.strip():
                if cur_elf_cals > max_elf_cals:
                    max_elf_cals = cur_elf_cals

                print(f"elf {elf_counter} has {cur_elf_cals}")
                print(f"The elf with the most food has {max_elf_cals} calories")

                elf_counter += 1
                cur_elf_cals = 0
            else:
                cur_elf_cals += int(line.strip())

    return max_elf_cals


def top_hungry_elves(input_file_path, top_n=3):
    with open(input_file_path) as calorie_list:
        current_elf_cals = 0
        leaderboard = [0] * top_n
        elf_counter = 0

        for line in calorie_list:
            if not line.strip():
                i = 0

                # go through the leaderboard as long as the current elf is not beating anyone
                while i < len(leaderboard) and current_elf_cals < leaderboard[i]:
                    i += 1
                # if we're done incrementing but not out of bounds, we found a new leader!
                if i < len(leaderboard):
                    # we insert and shift the list, the bottom value is now out of the leaderboard
                    leaderboard.insert(i, current_elf_cals)
                    leaderboard.pop()

                print(f"\nElf {elf_counter} has {current_elf_cals} calories")
                print("\nCalories leaderboard")
                for i in range(len(leaderboard)):
                    print(f"    {i}. {leaderboard[i]}")
                print("=====================================")
                elf_counter += 1
                current_elf_cals = 0
            else:
                current_elf_cals += int(line.strip())

    if elf_counter > top_n:
        leaderboard = leaderboard[:top_n]

    return sum(leaderboard)


