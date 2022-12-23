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


def test_Named_palette_exception():
    """Example test with parametrization."""
    p = palette.NamedPalette("Triad")
    with pytest.raises(TypeError):
        p["test"] = "#909090909"


def test_Linear_palette_exception():
    """Example test with parametrization."""
    p = palette.LinearPalette("Triad")
    with pytest.raises(TypeError):
        p.add("#909090909")


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


@pytest.mark.parametrize(
    ("name", "color_code"),
    [
        ("Primary", "#6750A4"),
        ("Primary", "6750A4"),
        ("Primary", 0x6750A4),
    ],
)
def test_material_ui_v3_Dark(name, color_code):
    """Matrial UI v3"""
    p = themes.MaterialDesignV3Dark()
    old = p[name]
    assert old == color_code


@pytest.mark.parametrize(
    ("name", "color_code"),
    [
        ("Background", "#222831"),
    ],
)
def test_bluewagon(name, color_code):
    """Matrial UI v3"""
    p = themes.BlueBlackWagon()
    old = p[name]
    assert old == color_code


@pytest.mark.parametrize(
    ("name", "color_code"),
    [
        ("Primary", "#D0BCFF"),
        ("Primary", "D0BCFF"),
        ("Primary", 0xD0BCFF),
    ],
)
def test_material_ui_v3_light(name, color_code):
    """Matrial UI v3"""
    p = themes.MaterialDesignV3Light()
    old = p[name]
    assert old == color_code


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
