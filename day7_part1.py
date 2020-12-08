import sys


def contains_bag_eventually(colors, current_color):
    if current_color == "shiny gold":
        return True

    does_contain_bag = False
    for v in colors[current_color]:
        does_contain_bag |= contains_bag_eventually(colors, v)
    return does_contain_bag


colors = {}

for line in sys.stdin:
    uniform_line = line.replace("bags", "bag").replace(
        ",", "bag").replace("contain", "").replace("contains", "")
    delimited = [s.strip() for s in uniform_line.split("bag")[:-1] if s]

    bag_color = delimited[0]
    colors[bag_color] = []

    for must_contain in delimited[1:]:
        number, color = must_contain.split(" ", 1)
        if number != "no":
            colors[bag_color].append(color)

count = sum(contains_bag_eventually(colors, color)
            for color in colors.keys()) - 1

print("# of bags that can eventually contain a shiny gold bag: {}".format(count))
