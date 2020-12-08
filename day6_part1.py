import sys

yes_count = 0
answers = set()

for line in sys.stdin.readlines() + ["\n"]:
    if line == "\n":
        yes_count += len(answers)
        answers = set()
    else:
        # Remove trailing newlines
        for c in line.rstrip():
            answers.add(c)

print(yes_count)
