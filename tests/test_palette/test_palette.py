import pytest

from py_colorpalette import color, palette, themes


@pytest.mark.parametrize(
    ("name", "color_code"),
    [
        ("primary", color.Color("850000")),
        ("secondary", "#808080"),
    ],
)
def test_get_set(name, color_code):
    """Example test with parametrization."""
    p = palette.NamedPalette("Triad")
    p[name] = color_code
    old = p[name]
    print("OLD", old, color_code)
    assert str(old) == str(color_code)


@pytest.mark.parametrize(
    ("name", "color_code"),
    [
        ("primary", color.Color("850000")),
        ("secondary", "#808080"),
    ],
)
def test_get_set_list_palette(name, color_code):
    """Example test with parametrization."""
    p = palette.LinearPalette("Triad")
    p.add(color_code)
    old = p[0]
    print("OLD", old, color_code)
    assert str(old) == str(color_code)


@pytest.mark.parametrize(
    ("name", "color_code"),
    [
        ("Deep Orange 200", "#FFAB91"),
        ("Blue Gray 900", "#263238"),
    ],
)
def test_material_ui(name, color_code):
    """Matrial UI"""
    p = themes.MaterialDesignV2()
    old = p[name]
    assert old == str(color_code)


def test_palette_index_error():
    """Linear Palette"""
    p = palette.LinearPalette("test")
    p.add("#434343")
    with pytest.raises(IndexError):
        p[2]

def test_palette_type_error():
    """Linear Palette"""
    p = palette.LinearPalette("test")
    p.add("#434343")
    with pytest.raises(TypeError):
        p["5t"]