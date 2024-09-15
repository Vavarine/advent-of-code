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

    is_game_possible = True

    for set in sets:
      cubes = set.split(", ")

      for cube in cubes:
        quantity, color = cube.split(" ")

        if(cubes_map[color] < int(quantity)): # surpass threshold
          is_game_possible = False
          break

    if(is_game_possible):
      total_sum += game_id

    # game_id = int(line.split(":")[0].split(" ")[1])
    # print(game_id)

print(total_sum)
    