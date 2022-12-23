"""Tests for Colors"""
import pytest

from py_colorpalette import color


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("AE12", False),
        ("#808080", True),
        ("808080", True),
        ("#K08080", False),
        (0x808080, True),
        (8421504, True),
        (None, False),
        (0x8080808,False)
    ],
)
def test_check_hex(code, expected):
    """Example test with parametrization."""
    assert color.check_hex(code) == expected

@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("#808080", color.Color("#808080")),
        (0x808080,"#808080")
    ],
)
def test_check_color(code, expected):
    """Example test with parametrization."""
    assert color.Color(code) == expected

def test_check_negative_color():
    """Example test with parametrization."""
    code = "#808080"
    assert (color.Color(code) == "#90909090") == False


def test_rgb_extract():
    c = color.Color("#807060")
    assert c.get_r() == 0x80
    assert c.get_g() == 0x70
    assert c.get_b() == 0x60


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("AE12", color.InvalidColorCodeException),
        ("#808080", "#808080"),
        ("808080", "#808080"),
        ("#FFFFFF", "#ffffff"),
        ("#K08080", color.InvalidColorCodeException),
        (0x808080, "#808080"),
        (8421504, "#808080"),
        ("54s125", color.InvalidColorCodeException),
        (0x808080,"#808080")
    ],
)
def test_format_hex(code, expected):
    """Example test with parametrization."""
    if not isinstance(expected, (str, int)):
        with pytest.raises(expected):
            assert color.format_hex(code)
    else:
        #print("FOrmat Hex: ", code, color.format_hex(code))
        assert color.format_hex(code) == expected


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("#808080", (128, 128, 128)),
    ],
)
def test_extract_hex(code, expected):
    """Example test with parametrization."""
    assert color.extract_hex(code) == expected
