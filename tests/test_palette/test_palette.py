import pytest

from py_colorpalette import color, palette


@pytest.mark.parametrize(
    ("name", "color_code"),
    [
        ( "primary" , color.Color("850000")),
        ( "secondary" , "#808080"),
    ],
)
def test_get_set(name, color_code):
  """Example test with parametrization."""
  p = palette.Palette("Triad")
  p[name] = color_code
  old = p[name]
  print("OLD",old, color_code)
  assert str(old) == str(color_code)
