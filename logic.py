from tile import Tile, Wind

def sort(tiles: list[Tile]) -> list[Tile]:
  return sorted(tiles, key=lambda tile: (tile.suit, tile.value))

# Checks if the given Tiles complete a set
def isSet(tiles: list[Tile]) -> bool:
  if len(tiles) != 3:
    return False
  return isTriplet(tiles) or isSeries(tiles)

 # Tile equality operations
def isDouble(tiles: list[Tile]) -> bool:
  if len(tiles) != 2:
    return False
  return isAllSame(tiles)

def isTriplet(tiles: list[Tile]) -> bool:
  if len(tiles) != 3:
    return False
  return isAllSame(tiles)

def isAllSame(tiles: list[Tile]) -> bool:
  for tile in tiles:
    if tile != tiles[0]:
      return False
  return True

# Checks if the given tiles form a consecutive series
def isSeries(tiles: list[Tile]) -> bool:
  tiles = sort(tiles)
  
  # Honour tiles cannot form a series
  if tiles[0].isHonour():
    return False
  
  for i, tile in enumerate(tiles):
    if i == 0:
      continue
    
    # All suits should be the same
    if tile.suit != tiles[0].suit:
      return False
    
    # Current tile value should be 1 higher than previous
    if tile.value != tiles[i-1].value + 1:
      return False
    
  return True

# Defines a basic method of calculating if a set of tiles constitutes a
# winning mahjong hand. There can be any number of tiles.
def isWinningHand(tiles: list[Tile]) -> bool:  
  tiles = sort(tiles)
  # print(tiles)
  visited = [0 for _ in range(len(tiles))]
  return isWinningHandHelper(tiles, visited, [tiles[0]], 0, False)
  
def isWinningHandHelper(
  tiles: list[Tile],
  visited: list[int],
  currentSet: list[Tile],
  currentIndex: int,
  hasFoundEye: bool,
) -> bool:
  # Mark current tile as visited
  visited = visited.copy()
  visited[currentIndex] = 1
  # print(visited, currentIndex, currentSet)
  
  # Try to resolve current set as an eye
  if not hasFoundEye and isDouble(currentSet):
    if isWinningHandHelper(tiles, visited, [], currentIndex, True):
      # Using this eye, managed to find a winning hand
      print(currentSet)
      return True
  
  # Try to resolve the current set
  if isSet(currentSet):
    if isWinningHandHelper(tiles, visited, [], currentIndex, hasFoundEye):
      # Using this completed set as a set, managed to find a winning hand
      print(currentSet)
      return True
  elif len(currentSet) >= 3:
    # Not a set but looking at 3 tiles, return to find another path
    return False
  
  # If no more tiles to visit
  if isAllVisited(visited):
    if len(currentSet) == 0:
      # Not in the middle of building a set, so this is a winning hand
      return True
    # Finished visiting all tiles but haven't finished building last set
    return False
  
  # Find the next unvisited tile
  for i, tile in enumerate(tiles):
    if visited[i]:
      continue
    
    if not isWinningHandHelper(tiles, visited, currentSet + [tile], i, hasFoundEye):
      # Couldn't find a winning combination, continue to try next tile
      continue
    
    # Found a winning hand combination
    return True
  
  # No winning hands found
  return False

def isAllVisited(visited: list[bool]) -> bool:
  for v in visited:
    if not v:
      return False
  return True