from enum import IntEnum
from functools import total_ordering

class Suit(IntEnum):
  Wan = 1
  Suo = 2
  Tong = 3
  Wind = 4
  Dragon = 5
  
class Wind(IntEnum):
  East = 1
  South = 2
  West = 3
  North = 4
  
class Dragon(IntEnum):
  Green = 1
  Red = 2
  White = 3

@total_ordering
class Tile:
  def __init__(self, suit: Suit, value: int):
    self.suit = suit
    self.value = value
    
  def __eq__(self, other):
    return self.suit == other.suit and self.value == other.value
  
  def __repr__(self):
    if isinstance(self.value, IntEnum):
      return "{0} {1}".format(self.value.name, self.suit.name)
    
    return "{0} {1}".format(self.value, self.suit.name)
  
  def __lt__(self, other):
    return self.suit < other.suit and self.value < other.value
  
  def __le__(self, other):
    return self.suit <= other.suit and self.value <= other.value
  
  def __gt__(self, other):
    return self.suit > other.suit and self.value > other.value
  
  def __ge__(self, other):
    return self.suit >= other.suit and self.value >= other.value
  
  def isHonour(self) -> bool:
    return self.suit >= 4
