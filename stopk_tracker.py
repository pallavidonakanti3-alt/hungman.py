# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("--------------------------")

while True:

    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not available.")
        print("Available stocks:", ", ".join(stock_prices.keys()))
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    except ValueError:
        print("Please enter a valid number.")

print("\n📊 Portfolio Summary")
print("--------------------")

for stock, quantity in portfolio.items():

    price = stock_prices[stock]
    value = price * quantity

    total_investment += value

    print(
        stock,
        "- Quantity:", quantity,
        "- Price: $", price,
        "- Value: $", value
    )

print("--------------------")
print("💰 Total Investment: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:

    file.write("Stock Portfolio Summary\n")
    file.write("-----------------------\n")

    for stock, quantity in portfolio.items():

        price = stock_prices[stock]
        value = price * quantity

        file.write(
            f"{stock} - Quantity: {quantity} - "
            f"Price: ${price} - Value: ${value}\n"
        )

    file.write("-----------------------\n")
    file.write(f"Total Investment: ${total_investment}\n")

print("\n✅ Portfolio saved to portfolio.txt")