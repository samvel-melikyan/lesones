import pytest
from calculator import Calculator

class TestCalc:

        def setup(self):
            self.calc = Calculator()


        def test_sum(self):
            assert 2+2==4

        def test_adding_success(self):
            assert self.calc.adding(self, 1, 2) == 2

        def test_adding_unsuccess(self):
            assert self.calc.adding(self, 1, 2) == 3

        def test_zero_division(self):
            with pytest.raises(ZeroDivisionError):
                self.calc.division(self, 1, 0)


        def teardown(self):
                print("«Выполнение метода teardown»)")