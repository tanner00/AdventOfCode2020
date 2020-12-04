# Explanation

# I do not like this extension of the problem because it is basically
# busy work, but it is a simple extension of the previous part.

# Basically just add each key, value pair of the passport fields to a table
# and check each set of rules individually. Some of this work can be compressed,
# like checking the length of some fields.

import sys

REQUIRED_FIELDS = {"byr", "iyr", "eyr",
                   "hgt", "hgt", "hcl", "ecl", "pid"}

valid_passports = 0
present_fields = set()
full_passport = {}

# Add a newline to the end of the file to signify a full passport at the end.
for line in sys.stdin.readlines() + ["\n"]:
    if line == "\n":
        valid_passport = True
        for rf in REQUIRED_FIELDS:
            if rf not in present_fields:
                valid_passport = False
                break

        for key, value in full_passport.items():
            if key in {"byr", "iyr", "eyr"} and len(value) != 4:
                valid_passport = False

            if not valid_passport:
                break

            if key == "byr":
                age = int(value)
                if age < 1920 or age > 2002:
                    valid_passport = False
            elif key == "iyr":
                issue_year = int(value)
                if issue_year < 2010 or issue_year > 2020:
                    valid_passport = False
            elif key == "eyr":
                expiration_year = int(value)
                if expiration_year < 2020 or expiration_year > 2030:
                    valid_passport = False
            elif key == "hgt":
                if len(value) < 3:
                    valid_passport = False
                    break

                height = int(value[:len(value) - 2])
                if value[-2:] == "cm":
                    if height < 150 or height > 193:
                        valid_passport = False
                elif value[-2:] == "in":
                    if height < 59 or height > 76:
                        valid_passport = False
                else:
                    valid_passport = False
            elif key == "hcl":
                if len(value) != 7 and value[0] != "#":
                    valid_passport = False
                    break

                if not value[1:].isalnum():
                    valid_passport = False
            elif key == "ecl":
                if value not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                    valid_passport = False
            elif key == "pid":
                if len(value) != 9 or not value.isnumeric():
                    valid_passport = False

        if valid_passport:
            valid_passports += 1

        # Reset the present fields for the next passport.
        present_fields = set()
        full_passport = {}

    split_line = line.split()
    for s in split_line:
        key, value = s.split(":")
        full_passport[key] = value

    fields = [l.split(":")[0] for l in split_line]
    present_fields.update(fields)

print("Number of valid passports according to the required fields: {}".format(
    valid_passports))
