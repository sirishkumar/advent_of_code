from utils import Position, get_command

if __name__ == "__main__":
  pos = Position()
  for cmd in get_command("input.txt"):
    pos.update_position_1(cmd)
  print(pos)
  print(f"Result={pos.x * pos.y}")
