import pytest
from main import Operator

test_example = Operator(4, 2)
def test_one():
    assert test_example.adding() == 5

def test_two():
    assert test_example.subtracting() == 2

if __name__ == '__main__':
    test_one()
    test_two()