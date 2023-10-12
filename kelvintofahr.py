import pytest

def test_kelvintofahr():
    kelvin = 22  
    fahrenheit = 1.8*(kelvin-273)+32
    assert fahrenheit == -419.8

if __name__ == "__main__":
    pytest.main()

