import pytest

from calculator.operations import calculator, CalculatorError

def test_reset():
    calc = calculator(10)

    calc.reset()

    assert calc.memory == 0
    

def test_add():
    calc = calculator(10)

    result = calc.add(2)

    assert result == 12

def test_subtract():
    calc = calculator(7)

    result = calc.subtract(3)

    assert result == 4

def test_multiply():
    calc = calculator(9)

    result = calc.multiply(3)

    assert result == 27

def test_divide():
    calc = calculator(9)

    result = calc.divide(3)

    assert result == 3

def test_root():
    calc = calculator(9)

    result = calc.root(2)

    assert result == 3

def test_power():
    calc = calculator(3)

    result = calc.root(3)

    assert result == 27

def test_divide_by_zero():
    calc = calculator(27)

    with pytest.raises(CalculatorError):
        calc.divide(0)

def test_zeroth_root():
    calc = calculator(27)

    with pytest.raises(CalculatorError):
        calc.root(0)

def test_stringy_init():
    with pytest.raises(CalculatorError):
        calc = calculator("ten")

def test_stringy_input():
    calc = calculator(3)
    
    with pytest.raises(CalculatorError):
        calc.multiply("three")
