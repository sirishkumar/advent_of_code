from enum import Enum, auto
from dataclasses import dataclass
from typing import Generator

class Direction(Enum):
  FORWARD = auto()
  DOWN = auto()
  UP = auto()

  @classmethod
  def value_of(cls, dir: str) -> "Direction":
    if dir == "forward":
      return cls.FORWARD

    if dir == "down":
      return cls.DOWN

    if dir == "up":
      return cls.UP


@dataclass
class Command:
  dir: Direction
  magnitude: int

  def __init__(self, dir: str, mag: str):
    self.dir = Direction.value_of(dir)
    self.mag = int(mag)

def get_command(file_name: str) -> Generator[Command, None, None]:
  with open(file_name) as fp:
    for line in fp:
      dir, mag = line.split()
      yield Command(dir, mag)
   

@dataclass
class Position:
  y: int = 0
  x: int = 0
  aim: int = 0

  def __repr__(self):
    return f"Position(x={self.x}, y={self.y}, aim={self.aim})"

  def update_position_1(self, cmd: Command):
    if cmd.dir == Direction.FORWARD:
      self.x += cmd.mag
    elif cmd.dir == Direction.UP:
      self.y -= cmd.mag
    elif cmd.dir == Direction.DOWN:
      self.y += cmd.mag

  def update_position_2(self, cmd: Command):
    if cmd.dir == Direction.FORWARD:
      self.x += cmd.mag
      self.y += (self.aim * cmd.mag)
    elif cmd.dir == Direction.DOWN:
      self.aim += cmd.mag
    elif cmd.dir == Direction.UP:
      self.aim -= cmd.mag

