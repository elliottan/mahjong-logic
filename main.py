import sys

from constants import *
from logic import *
from randomlogic import *

def main() -> int:
  # print(isSet([WAN[5], WAN[3], WAN[4]]))
  # tiles = [TONG[4], TONG[3], TONG[2]]
  # print(tiles)
  # print(isSet(tiles))
  
  hand = [
    WAN[1], WAN[2], TONG[8],
    SUO[6], SUO[7], SUO[5], WAN[3],
    TONG[3],
    DRAGON[Dragon.Red],
    TONG[3],
    DRAGON[Dragon.Red],
    TONG[9],
    DRAGON[Dragon.Red],
    TONG[7]
  ]
  i = 0
  
  while True:
    i += 1
    if i % 1000 == 0:
      print(i)
  
    hand = getRandomTiles(11)
    if isWinningHand(hand):
      print(i)
      print(sort(hand))
      break
  
  return 0

if __name__ == '__main__':
    sys.exit(main())