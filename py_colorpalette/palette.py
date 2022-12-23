from typing import Any

try:
  from py_colorpalette import color
except ModuleNotFoundError:
  import color

class Palette():
  def __init__(self, name:str) -> None:
    self.palette_name = name
    self.named_palette = {}
    self.colors = []
  def __getitem__(self, __name: str) -> color.Color:
    return self.named_palette[__name]
  
  def __setitem__(self, name: str, value: Any) -> None:
    print(name,value)
    if not isinstance(value, color.Color):
      try:
        value = color.Color(value)
      except color.InvalidColorCodeException:
        raise TypeError(f"The item {value} [{type(value)}] is not a color. Use Color().") 
    self.named_palette[name] = value
  

# if __name__ == "__main__":
#   name = "primary"
#   color_code = "850000"
#   p = Palette("Triad")
#   p[name] = color.Color(color_code)
#   assert str(p[name]) == color.format_hex(color_code)