from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, value: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply(self, value: float) -> float:
        return value


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply(self, value: float) -> float:
        return value - (value * (self.percent / 100.0))


class CouponDiscount(DiscountStrategy):
    def __init__(self, discount: float):
        self.discount = discount

    def apply(self, value: float) -> float:
        return max(0.0, value - self.discount)


class DiscountCalculator:
    def calculate(self, value: float, policy: str, discount_val: float = 0.0) -> float:
        if policy == "PERCENTAGE":
            strategy = PercentageDiscount(discount_val)
        elif policy == "COUPON":
            strategy = CouponDiscount(discount_val)
        else:
            strategy = NoDiscount()

        return strategy.apply(value)