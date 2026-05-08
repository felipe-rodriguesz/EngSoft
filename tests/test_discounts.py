import unittest
from calculator import DiscountCalculator

class TestDiscountCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = DiscountCalculator()

    def test_no_discount(self):
        # Sem desconto: retorna o valor original [cite: 14, 15]
        self.assertEqual(self.calc.calculate(100.0, 'NONE'), 100.0)

    def test_percentage_discount(self):
        # Desconto percentual: aplica um percentual fixo [cite: 16]
        self.assertEqual(self.calc.calculate(100.0, 'PERCENTAGE', 10.0), 90.0)

    def test_coupon_discount(self):
        # Desconto por cupom: subtrai um valor fixo [cite: 16]
        self.assertEqual(self.calc.calculate(100.0, 'COUPON', 20.0), 80.0)

    def test_coupon_discount_never_negative(self):
        # Desconto por cupom: nunca resultando em valor negativo [cite: 16]
        self.assertEqual(self.calc.calculate(10.0, 'COUPON', 20.0), 0.0)

if __name__ == '__main__':
    unittest.main()