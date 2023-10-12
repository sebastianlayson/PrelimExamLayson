import pytest

def test_rectangleArea():
    width = 10
    height = 6
    computed = width*height
    area = 50
    assert area == computed

if __name__ == "__main__":
    pytest.main()
