import pytest


def test_weight():
    weight = 81 
    assert weight >= 80 

def test_kelvintofahr():
    kelvin = 22  
    fahrenheit = 1.8*(kelvin-273)+32
    assert fahrenheit == -419.8

def test_rectangleArea():
    width = 10
    height = 5
    computed = width*height
    area = 50
    assert area == computed

if __name__ == "__main__":
    pytest.main()
