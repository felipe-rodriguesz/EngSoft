class DiscountCalculator:
    def calculate(self, value: float, policy: str, discount_val: float = 0.0) -> float:
        if policy == 'PERCENTAGE':
            return value - (value * (discount_val / 100.0))
        elif policy == 'COUPON':
            return max(0.0, value - discount_val)
        
        # Sem desconto
        return value