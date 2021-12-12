from tile import *

TILES = [None] * (27 + 7) # Initialise each tile with a unique index ID

# Initialise tile values as they are constants in mahjong
WAN = {}; SUO = {}; TONG = {}; WIND = {}; DRAGON = {}

id = 0
for val in range(1, 10):
  WAN[val] = Tile(Suit.Wan, val)
  SUO[val] = Tile(Suit.Suo, val)
  TONG[val] = Tile(Suit.Tong, val)
  
  TILES[id] = WAN[val]      # 0-8: wan
  TILES[id+9] = SUO[val]    # 9-17: suo
  TILES[id+18] = TONG[val]  # 18-26: tong
  id += 1

id = 27
for wind in Wind:
  WIND[wind] = Tile(Suit.Wind, wind)
  TILES[id] = WIND[wind]
  id += 1

for dragon in Dragon:
  DRAGON[dragon] = Tile(Suit.Dragon, dragon)
  TILES[id] = DRAGON[dragon]
  id += 1
