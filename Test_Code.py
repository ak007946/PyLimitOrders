class Order:
    def __init__(self, order_type, product_id, amount, limit_price):
        self.order_type = order_type  # 'buy' or 'sell'
        self.product_id = product_id
        self.amount = amount
        self.limit_price = limit_price

    def __repr__(self):
        return f"{self.order_type.capitalize()} {self.amount} shares of {self.product_id} at ${self.limit_price}"

class LimitOrderAgent:
    def __init__(self):
        self.orders = []  # List to hold orders

    def add_order(self, order_type, product_id, amount, limit_price):
        """Add an order to the agent's order list."""
        if order_type not in ['buy', 'sell']:
            raise ValueError("Order type must be 'buy' or 'sell'")
        if amount <= 0 or limit_price <= 0:
            raise ValueError("Amount and limit price must be positive values")

        order = Order(order_type, product_id, amount, limit_price)
        self.orders.append(order)
        print(f"Added order: {order}")

    def execute_orders(self, market_price, product_id):
        """Execute orders based on the market price and product ID."""
        for order in self.orders[:]:  # Iterate over a copy of the list
            if order.product_id == product_id:
                if order.order_type == 'buy' and market_price <= order.limit_price:
                    print(f"Executing {order}")
                    self.orders.remove(order)
                elif order.order_type == 'sell' and market_price >= order.limit_price:
                    print(f"Executing {order}")
                    self.orders.remove(order)

# Example usage
if __name__ == "__main__":
    agent = LimitOrderAgent()
    
    # Adding orders
    agent.add_order('buy', 'IBM', 1000, 100)
    agent.add_order('sell', 'IBM', 500, 150)
    
    # Market prices
    market_price_ibm = 99  # Example market price for IBM

    # Execute orders based on market prices
    print("Market price for IBM is $99")
    agent.execute_orders(market_price_ibm, 'IBM')
    
    # Testing with a different market price
    market_price_ibm = 101  # Example market price for IBM
    print("Market price for IBM is $101")
    agent.execute_orders(market_price_ibm, 'IBM')
