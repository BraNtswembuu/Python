# Create a shopping cart programme that will continuously ask the user for a food product and the price of that product
# Have an exit clause if the user wishes to stop adding more things to their cart
# At the end show the food items and the total cost to the user

def shopping_cart_merged():
    """
    Manages a simple shopping cart, allowing users to add items and view the total cost.
    Merges ideas from provided user code and enhanced version.
    """
    # Using a list of dictionaries to store each item's product name and price together
    shopping_cart_items = []
    total_cost = 0.0 # Initialize total_cost to 0.0 for accurate sum

    print("Welcome to your Shopping Cart!")
    print("Enter 'q' for the product name to quit.")

    while True:
        # Get product name input - using your prompt style
        food_name = input("Enter a food to buy or press 'q' to quit: ").strip()

        # Check for the exit condition using your 'q' approach
        if food_name.lower() == 'q':
            break # Exit the loop if user types 'q'

        # --- Get product price input with validation (from my suggestion) ---
        while True: # Loop to ensure valid price input
            price_input = input(f"Enter the price of the {food_name}: R")
            try:
                product_price = float(price_input)
                if product_price < 0:
                    print("Price cannot be negative. Please enter a valid price.")
                else:
                    break # Valid price, exit inner loop
            except ValueError:
                print("Invalid price. Please enter a number (e.g., 15.50 or 20).")

        # Add the item as a dictionary to our list
        item = {"product": food_name, "price": product_price}
        shopping_cart_items.append(item)
        print(f"'{food_name}' (R{product_price:.2f}) added.") # Confirmation message

    # --- Display YOUR CART and Total ---
    print("\n----- YOUR CART -----")
    if not shopping_cart_items: # Check if the cart is empty
        print("Your cart is empty.")
    else:
        # Iterate through the list of dictionaries to display items and calculate total
        for item in shopping_cart_items:
            print(f"{item['product']:<20} R{item['price']:.2f}")
            total_cost += item['price'] # Sum up the total cost here as we iterate

    print("---------------------")
    # Display the final total cost
    print(f"Your total is:      R{total_cost:.2f}")
    print("Thank you for shopping with us!")


# Call the function to run the shopping cart
if __name__ == "__main__":
    shopping_cart_merged()