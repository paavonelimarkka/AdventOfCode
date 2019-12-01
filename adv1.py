# Advent of Code - Day 1, puzzle 1
# https://adventofcode.com/2019/day/1

# Part 1

contents = [int(i) for i in open("day1_input.txt").readlines()]

for i in range(len(contents)):
    contents[i] = int(contents[i] // 3 - 2)

full = sum(contents)
print(f"First part: Elves require {full} liters of fuel!")

# Part 2

modules = [int(i) for i in open("day1_input.txt").readlines()]

totalweight = []

for i in range(len(modules)):
    leftover_list = []
    leftover_list.append(int(modules[i] // 3 - 2))
    
    while (leftover_list[-1] > 5):
        leftover_list.append(leftover_list[-1] // 3 - 2)

    totalweight.append(sum(leftover_list))

print(f"Second part: Elves ACTUALLY require {sum(totalweight)} liters of fuel!")