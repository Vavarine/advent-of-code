import requests
import os
import re
from dotenv import load_dotenv

load_dotenv()

cookies = {"session": os.getenv("SESSION_TOKEN")}

url = "https://adventofcode.com/2023/day/1/input"
response = requests.get(url, cookies=cookies).text

total_sum = 0

for line in response.splitlines():
  numbers_in_line = re.findall(r'\d', line)
  total_sum += int(numbers_in_line[0] + numbers_in_line[-1])


print(total_sum)