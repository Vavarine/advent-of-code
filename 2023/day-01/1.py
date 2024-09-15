import re

total_sum = 0

with open('input.txt', 'r') as file:
  for line in file:
    numbers_in_line = re.findall(r'\d', line)
    total_sum += int(numbers_in_line[0] + numbers_in_line[-1])


print(total_sum)