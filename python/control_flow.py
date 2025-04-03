def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if applicable.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage
    
    Returns:
        float: The final price after discount (if applicable)
    """
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    return price

# Get user input
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Display results
    if final_price < original_price:
        print(f"Final price after {discount_percentage}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Original price: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")