import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculator_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculator_correctly(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_adding_calculator_correctly(self):
        assert self.calc.adding(self, 30, 10) == 40

    def test_subtraction_calculator_correctly(self):
        assert self.calc.subtraction(self, 34, 30) == 4
