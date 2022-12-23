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
        (0x808080,True),
        (8421504, True),
        (None, False)
    ],
)
def test_check_hex(code, expected):
    """Example test with parametrization."""
    assert color.check_hex(code) == expected

@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("AE12", color.InvalidColorCodeException),
        ("#808080", "#808080"),
        ("808080", "#808080"),
        ("#FFFFFF", "#ffffff"),
        ("#K08080", color.InvalidColorCodeException),
        (0x808080,"#808080"),
        (8421504, "#808080"),
        ("54s125", color.InvalidColorCodeException)
    ],
)
def test_format_hex(code, expected):
    """Example test with parametrization."""
    if not isinstance(expected,(str,int)):
        with pytest.raises(expected):
          assert color.format_hex(code)
    else:
      assert color.format_hex(code) == expected

@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("#808080", (128,128,128)),
    ],
)
def test_extract_hex(code, expected):
    """Example test with parametrization."""
    assert color.extract_hex(code) == expected
