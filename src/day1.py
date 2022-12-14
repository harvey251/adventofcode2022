# pylint: skip-file
from pathlib import Path

elf = 1
elf_total = 0
t_elf = 1
t_total = 0

elves = []

with Path(__file__).parent.joinpath("day1_input.txt").open("r") as f:
    for line in f.readlines():
        total_str = line.strip()
        if total_str and total_str.isdigit():
            t_total += int(total_str)
            continue

        if t_total > elf_total:
            elf_total = t_total
            elf = t_elf

        elves.append((t_total, t_elf))

        t_elf += 1
        t_total = 0

print(elf, elf_total)

total = sum(i for i, _ in sorted(elves)[-3:])
print(total)
