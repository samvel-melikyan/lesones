from apps.calc import Calculator
import pytest

# noinspection PyTypeChecker
class TestCalc:
    def setup_method(self):
        self.calc = Calculator()

    def test_adding_success(self):
        assert self.calc.adding(1, 1) == 2

    def test_adding_unsuccess(self):
        assert not self.calc.adding(1, 2) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown_method(self):
        print("Выполнение метода teardown")
