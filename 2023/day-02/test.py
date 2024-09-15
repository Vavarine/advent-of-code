cubes = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

def above_threshold(color, quantity): 
  if(cubes[color] < quantity): return True

  return False

print(above_threshold('red', 13))