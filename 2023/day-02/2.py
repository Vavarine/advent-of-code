total_sum = 0

cubes_map = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

with open('input.txt', 'r') as file:
  for line in file:
    line = line.removeprefix("Game ").removesuffix("\n")
    game_id = int(line.split(": ")[0])
    sets = line.split(": ")[1].split("; ")

    min_possible_cube_colors = {
      'red': 0,
      'green': 0,
      'blue': 0,
    }

    for set in sets:
      cubes = set.split(", ")

      for cube in cubes:
        quantity, color = cube.split(" ")
        quantity = int(quantity)

        if min_possible_cube_colors[color] < quantity:
          min_possible_cube_colors[color] = quantity
        
    power = 1

    for color in min_possible_cube_colors:
      power *= min_possible_cube_colors[color]

    total_sum += power

    # game_id = int(line.split(":")[0].split(" ")[1])
    # print(game_id)

print(total_sum)
    