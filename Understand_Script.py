import csv, re, math, sys

csv_file = csv.reader(sys.stdin)
next(csv_file)

with open('Understand_Output.txt', 'w') as file:

    for line in csv_file:
        from_file = line[0]
        to_file = line[1].split("/")
        to_file = to_file[-1]
        entry = from_file + " -> " + to_file + "\n"
        file.write(entry)
