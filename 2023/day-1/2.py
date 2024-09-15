import requests
import os
import re
from dotenv import load_dotenv

load_dotenv()

cookies = {"session": os.getenv("SESSION_TOKEN")}

url = "https://adventofcode.com/2023/day/1/input"

response = requests.get(url, cookies=cookies).text

def get_first_digit_on_string(string):
  digit_names = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
  }

  for digit in digit_names:
    string = string.replace(digit_names[digit],  digit_names[digit] + str(digit))

  numbers_in_line = re.findall(r'\d', string)

  if(len(numbers_in_line) > 0): return numbers_in_line[0]

  return -1 

def main(string): 
  total_sum = 0
  for line in string.splitlines():
    firstDigit = -1
    lastDigit = -1

    count = 0

    while (firstDigit == -1 or lastDigit == -1) and count < len(line):
      count += 1

      if(firstDigit == -1):
        firstDigit = get_first_digit_on_string(line[:count])

      if(lastDigit == -1):
        lastDigit = get_first_digit_on_string(line[-count:])

    total_sum += int(firstDigit + lastDigit)

  return total_sum

print(main(response))