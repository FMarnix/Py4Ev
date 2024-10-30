import re

hand = open('regex_sum_1232985.txt')
total_sum = 0
for line in hand:
    line = line.rstrip()
    numbers = re.findall(r'\d+', line)
    total_sum += sum(map(int, numbers))

print(total_sum)