import random
from tile import Tile
from constants import TILES

# Gets n number of random tiles with replacement
def getRandomTiles(n: int) -> list[Tile]:
  return [TILES[random.randint(0, len(TILES)-1)] for _ in range(n)]

# TODO: another get random tile without replacement
