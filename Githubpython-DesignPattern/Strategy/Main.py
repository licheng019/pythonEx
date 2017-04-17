from FedexStrategy import FedexStrategy
from ShippingCost import ShippingCost
from Order import Order

order = Order()
strategy = FedexStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
print cost