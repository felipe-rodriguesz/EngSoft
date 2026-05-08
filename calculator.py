from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    # Interface da estrategia: encapsula o comportamento de desconto
    @abstractmethod
    def apply(self, value: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    # Estrategia concreta: nao altera o valor
    def apply(self, value: float) -> float:
        return value


class PercentageDiscount(DiscountStrategy):
    # Estrategia concreta: desconto por percentual
    def __init__(self, percent: float):
        self.percent = percent

    def apply(self, value: float) -> float:
        return value - (value * (self.percent / 100.0))


class CouponDiscount(DiscountStrategy):
    # Estrategia concreta: desconto de valor fixo
    def __init__(self, discount: float):
        self.discount = discount

    def apply(self, value: float) -> float:
        return max(0.0, value - self.discount)


class DiscountCalculator:
    # Contexto: seleciona a estrategia sem mudar a API publica
    def calculate(self, value: float, policy: str, discount_val: float = 0.0) -> float:
        # Selecao dinamica da estrategia conforme a politica
        if policy == "PERCENTAGE":
            strategy = PercentageDiscount(discount_val)
        elif policy == "COUPON":
            strategy = CouponDiscount(discount_val)
        else:
            strategy = NoDiscount()

        return strategy.apply(value)