import pytest
from src.math_operations import MathOperations


@pytest.fixture
def math_ops():
    return MathOperations()


def test_add(math_ops):
    assert math_ops.add(10, 5) == 15
    assert math_ops.add(-1, 1) == 0


def test_subtract(math_ops):
    assert math_ops.subtract(10, 5) == 5
    assert math_ops.subtract(5, 10) == -5


def test_multiply(math_ops):
    assert math_ops.multiply(3, 4) == 12
    assert math_ops.multiply(0, 5) == 0


def test_divide(math_ops):
    assert math_ops.divide(10, 2) == 5
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        math_ops.divide(10, 0)


def test_power(math_ops):
    assert math_ops.power(2, 3) == 8
    assert math_ops.power(5, 0) == 1


def test_square_root(math_ops):
    assert math_ops.square_root(9) == 3
    with pytest.raises(
        ValueError, match="Cannot calculate square root of negative number."
    ):
        math_ops.square_root(-1)


def test_factorial(math_ops):
    assert math_ops.factorial(5) == 120
    assert math_ops.factorial(0) == 1
    with pytest.raises(
        ValueError, match="Cannot calculate factorial of negative number."
    ):
        math_ops.factorial(-1)
