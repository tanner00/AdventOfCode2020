import sys

all_yes_count = 0
answers = [0] * 26
people_in_group = 0

for line in sys.stdin.readlines() + ["\n"]:
    if line == "\n":
        for i in range(26):
            if answers[i] == people_in_group:
                all_yes_count += 1

        answers = [0] * 26
        people_in_group = 0
    else:
        # Remove trailing newlines
        for c in line.rstrip():
            answers[ord(c) - ord('a')] += 1
        people_in_group += 1

print(all_yes_count)
