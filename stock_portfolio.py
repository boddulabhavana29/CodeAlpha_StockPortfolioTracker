
# CodeAlpha Task 2: Stock Portfolio Tracker
# Calculates investment value and profit or loss

portfolio = []

print("=" * 45)
print("   STOCK PORTFOLIO TRACKER")
print("=" * 45)

while True:
    stock_name = input("\nEnter stock name (or 'done' to finish): ").strip()

    if stock_name.lower() == "done":
        break

    try:
        quantity = int(input("Enter quantity of shares: "))
        purchase_price = float(input("Enter purchase price per share: "))
        current_price = float(input("Enter sample current price per share: "))

        if quantity <= 0 or purchase_price < 0 or current_price < 0:
            print("Please enter valid positive values.")
            continue

        investment = quantity * purchase_price
        current_value = quantity * current_price
        profit_loss = current_value - investment

        stock = {
            "name": stock_name,
            "quantity": quantity,
            "investment": investment,
            "current_value": current_value,
            "profit_loss": profit_loss
        }

        portfolio.append(stock)
        print("Stock added successfully!")

    except ValueError:
        print("Invalid input. Please enter numbers for quantity and prices.")

if len(portfolio) == 0:
    print("\nNo stocks were added.")

else:
    total_investment = 0
    total_current_value = 0
    total_profit_loss = 0

    print("\n" + "=" * 65)
    print("             YOUR PORTFOLIO REPORT")
    print("=" * 65)

    for stock in portfolio:
        print("\nStock:", stock["name"])
        print("Quantity:", stock["quantity"])
        print("Investment: Rs.", round(stock["investment"], 2))
        print("Current value: Rs.", round(stock["current_value"], 2))

        if stock["profit_loss"] > 0:
            print("Status: PROFIT")
        elif stock["profit_loss"] < 0:
            print("Status: LOSS")
        else:
            print("Status: NO PROFIT, NO LOSS")

        print("Profit/Loss: Rs.", round(stock["profit_loss"], 2))

        total_investment += stock["investment"]
        total_current_value += stock["current_value"]
        total_profit_loss += stock["profit_loss"]

    print("\n" + "=" * 45)
    print("         TOTAL PORTFOLIO SUMMARY")
    print("=" * 45)
    print("Total investment: Rs.", round(total_investment, 2))
    print("Current value: Rs.", round(total_current_value, 2))
    print("Overall profit/loss: Rs.", round(total_profit_loss, 2))

    report = "\nSTOCK PORTFOLIO REPORT\n"
    report += "-" * 35 + "\n"

    for stock in portfolio:
        report += (
            f"Stock: {stock['name']}\n"
            f"Quantity: {stock['quantity']}\n"
            f"Investment: Rs. {stock['investment']:.2f}\n"
            f"Current Value: Rs. {stock['current_value']:.2f}\n"
            f"Profit/Loss: Rs. {stock['profit_loss']:.2f}\n\n"
        )

    report += f"Total Investment: Rs. {total_investment:.2f}\n"
    report += f"Current Value: Rs. {total_current_value:.2f}\n"
    report += f"Overall Profit/Loss: Rs. {total_profit_loss:.2f}\n"

    with open("portfolio_report.txt", "w") as file:
        file.write(report)

    print("\nReport saved as portfolio_report.txt")
    print("Thank you for using Stock Portfolio Tracker!")
