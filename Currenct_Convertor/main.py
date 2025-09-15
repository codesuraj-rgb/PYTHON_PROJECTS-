print("WELCOME IN CURRENCY CONVERTOR")

def currency_convertor():
    try:
        amount = float(input("Enter the amount : "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    print("Choose the currency to convert into:")
    print("1. USD")
    print("2. EUR")
    print("3. GBP")
    print("4. JPY")
    print("5. CHF")

    choice = input("Enter the option (1-5): ")

    if choice == "1":
        target_currency = "USD"
    elif choice == "2":
        target_currency = "EUR"
    elif choice == "3":
        target_currency = "GBP"
    elif choice == "4":
        target_currency = "JPY"
    elif choice == "5":
        target_currency = "CHF"
    else:
        print("Invalid choice. Please select a number between 1 and 5.")
        return

    print(f"You chose to convert INR to {target_currency}.")
    
    rates = {
        "USD": 0.011,  
        "EUR": 0.0095,
        "GBP": 0.0085,
        "JPY": 1.50,
        "CHF": 0.010
    }

    conversion_rate = rates[target_currency]
    converted_amount = amount * conversion_rate

    print(f"\n{amount} INR is equal to {converted_amount:.2f} {target_currency}")

currency_convertor()
