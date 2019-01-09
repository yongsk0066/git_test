in_file = open('chicken.txt', 'r')
line_count = 0
sum = 0

for line in in_file:
    data = line.strip().split(": ")
    amount = int(data[1])

    sum += amount
    line_count += 1

print(sum)
print(sum / line_count)

