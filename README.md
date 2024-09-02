class PriceError(Exception):
    """Custom exception for invalid price values."""
    pass

def should_sell_product(purchase_price, selling_price):
    """
    Determine if the product should be sold based on its selling price and purchase price.

    Parameters:
    purchase_price (float): The price at which the product was purchased.
    selling_price (float): The price at which the product is intended to be sold.

    Returns:
    bool: True if the product should be sold, False otherwise.
    """
    try:
        # Check for valid numeric input
        if not (isinstance(purchase_price, (int, float)) and isinstance(selling_price, (int, float))):
            raise PriceError("Prices must be numeric values.")
        
        # Check for negative prices
        if purchase_price < 0 or selling_price < 0:
            raise PriceError("Prices must be non-negative values.")
        
        # Determine if the product should be sold
        if selling_price < purchase_price:
            return False
        return True
    
    except PriceError as e:
        print(f"PriceError: {e}")
        return False

# Test cases
def test_should_sell_product():
    assert should_sell_product(100, 150) == True, "Test case 1 failed"
    assert should_sell_product(100, 100) == True, "Test case 2 failed"
    assert should_sell_product(100, 50) == False, "Test case 3 failed"
    assert should_sell_product(100, -50) == False, "Test case 4 failed"
    assert should_sell_product(-100, 150) == False, "Test case 5 failed"
    assert should_sell_product("100", 150) == False, "Test case 6 failed"
    assert should_sell_product(100, "150") == False, "Test case 7 failed"
    
    print("All test cases passed")

# Run test cases
test_should_sell_product()
