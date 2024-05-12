import pytest

class Calculator:
    def calculate_discount(self, purchase_amount, discount_percentage):
        if purchase_amount < 0 or discount_percentage < 0 or discount_percentage > 100:
            raise ArithmeticError("Invalid arguments: purchase_amount and discount_percentage must be non-negative, and discount_percentage must be between 0 and 100.")
        discount_amount = purchase_amount * discount_percentage / 100
        return purchase_amount - discount_amount

def test_calculate_discount():
    calculator = Calculator()

    assert calculator.calculate_discount(100, 10) == 90
    assert calculator.calculate_discount(200, 25) == 150

def test_calculate_discount_with_invalid_arguments():
    calculator = Calculator()

    with pytest.raises(ArithmeticError) as e:
        calculator.calculate_discount(-100, 10)
    assert str(e.value) == "Invalid arguments: purchase_amount and discount_percentage must be non-negative, and discount_percentage must be between 0 and 100."

    with pytest.raises(ArithmeticError) as e:
        calculator.calculate_discount(100, -10)
    assert str(e.value) == "Invalid arguments: purchase_amount and discount_percentage must be non-negative, and discount_percentage must be between 0 and 100."

    with pytest.raises(ArithmeticError) as e:
        calculator.calculate_discount(100, 110)
    assert str(e.value) == "Invalid arguments: purchase_amount and discount_percentage must be non-negative, and discount_percentage must be between 0 and 100."

if __name__ == '__main__':
    test_calculate_discount_with_invalid_arguments()