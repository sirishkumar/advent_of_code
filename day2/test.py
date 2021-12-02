import pytest

from utils import Command, Direction

def test_forward_command():
  cmd = Command("forward", 1)
  assert cmd.dir == Direction.FORWARD
  assert cmd.mag == 1


def test_up_command():
  cmd = Command("up", 2)
  assert cmd.dir == Direction.UP
  assert cmd.mag == 2


def test_down_command():
  cmd = Command("down", 8)
  assert cmd.dir == Direction.DOWN
  assert cmd.mag == 8


  