import sys

file_1 = open(sys.argv[1], 'r')
file_2 = open(sys.argv[2], 'r')
file_output = open("comparison_output.txt", 'w')
for line in file_1:
    # print("Line1:", line)
    file_2 = open(sys.argv[2], 'r')
    for line2 in file_2:
        # print("Line2:", line2)
        if line == line2:
            # print("yes")
            file_output.write(line)

file_output.close()

