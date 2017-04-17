from ShippingStrategy import ShippingStrategy

class FedexStrategy(ShippingStrategy):
    def calculate(self, order):
        return 3.00