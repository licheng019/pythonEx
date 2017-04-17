from ShippingStrategy import ShippingStrategy

class UPSStrategy(ShippingStrategy):
    def calculate(self, order):
        return 4.00