def add_or_update_product(sales_data, product_name, price, quantity_sold):
    """Adds a new product or updates an existing product's sales quantity and price."""
    for item in sales_data:
        if item["name"].lower() == product_name.lower():
            item["price"] = price
            item["quantity"] += quantity_sold
            print(
                f"Updated '{item['name']}': Added {quantity_sold} units (Total:"
                f" {item['quantity']})."
            )
            return

    sales_data.append(
        {"name": product_name, "price": price, "quantity": quantity_sold}
    )
    print(f"Added new product '{product_name}' to sales records.")


def analyze_sales(sales_data):
    """Calculates product revenues, total revenue, and identifies top performers."""
    if not sales_data:
        print("No sales data available.")
        return

    total_revenue = 0
    highest_revenue_product = None
    highest_qty_product = None

    print("\n" + "=" * 72)
    print(
        f"{'Product Name':<18} | {'Unit Price':<12} | {'Qty Sold':<10} |"
        f" {'Total Revenue':<15} | {'Share %'}"
    )
    print("-" * 72)

    # First pass to calculate total revenue
    for item in sales_data:
        item["revenue"] = item["price"] * item["quantity"]
        total_revenue += item["revenue"]

    # Second pass to display and compare performance
    for item in sales_data:
        rev = item["revenue"]
        share = (rev / total_revenue * 100) if total_revenue > 0 else 0

        if (
            highest_revenue_product is None
            or rev > highest_revenue_product["revenue"]
        ):
            highest_revenue_product = item

        if (
            highest_qty_product is None
            or item["quantity"] > highest_qty_product["quantity"]
        ):
            highest_qty_product = item

        print(
            f"{item['name']:<18} | ₹{item['price']:>10,.2f} |"
            f" {item['quantity']:>10} | ₹{rev:>13,.2f} | {share:>6.2f}%"
        )

    print("=" * 72)
    print(f"OVERALL TOTAL SALES REVENUE: ₹{total_revenue:,.2f}")
    print("-" * 72)
    print(
        f"Highest Revenue Generator : {highest_revenue_product['name']}"
        f" (₹{highest_revenue_product['revenue']:,.2f})"
    )
    print(
        f"Most Units Sold           : {highest_qty_product['name']}"
        f" ({highest_qty_product['quantity']} units)"
    )
    print("=" * 72)


# --- Testing Scenarios ---
if __name__ == "__main__":
    # Dataset 1: Electronics Store Sales (List of Dictionaries)
    electronics_sales = [
        {"name": "Wireless Mouse", "price": 799.00, "quantity": 45},
        {"name": "Mechanical Keyboard", "price": 2499.00, "quantity": 20},
        {"name": "USB-C Hub", "price": 1299.00, "quantity": 30},
        {"name": "27-inch Monitor", "price": 14500.00, "quantity": 8},
    ]

    print("--- DATASET 1: Electronics Store Performance ---")
    analyze_sales(electronics_sales)

    print("\n--- Updating Dataset 1 with New Sales & New Product ---")
    add_or_update_product(electronics_sales, "Wireless Mouse", 799.00, 25)
    add_or_update_product(electronics_sales, "Webcam 1080p", 3200.00, 15)
    analyze_sales(electronics_sales)

    # Dataset 2: Bookstore Sales (Testing with a different dataset)
    bookstore_sales = [
        {"name": "Python Programming", "price": 550.00, "quantity": 60},
        {"name": "Data Structures", "price": 480.00, "quantity": 42},
        {"name": "AI Fundamentals", "price": 850.00, "quantity": 35},
    ]

    print("\n--- DATASET 2: Bookstore Performance ---")
    analyze_sales(bookstore_sales)