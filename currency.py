from forex_python.converter import CurrencyRates
from tabulate import tabulate

def convert_currency():
    print("Welcome to the Currency Conversion Tool!")
    
    # Display available currencies
    currencies = {
        "United States": "USD", "European Union": "EUR",
        "Japan": "JPY", "United Kingdom": "GBP",
        "Switzerland": "CHF", "Australia": "AUD",
        "Canada": "CAD", "China": "CNY",
        "Sweden": "SEK", "Norway": "NOK",
        "South Korea": "KRW", "Singapore": "SGD",
        "New Zealand": "NZD", "Hong Kong": "HKD",
        "Denmark": "DKK", "India": "INR",
        "Brazil": "BRL", "Russia": "RUB",
        "South Africa": "ZAR", "Turkey": "TRY",
        "Mexico": "MXN", "Indonesia": "IDR",
        "Saudi Arabia": "SAR", "Argentina": "ARS",
        "Taiwan": "TWD", "Thailand": "THB",
        "Poland": "PLN", "Israel": "ILS",
        "Philippines": "PHP", "Malaysia": "MYR",
        "Czech Republic": "CZK", "Hungary": "HUF",
        "UAE": "AED", "Colombia": "COP",
        "Egypt": "EGP", "Chile": "CLP",
        "Romania": "RON", "Nigeria": "NGN",
        "Pakistan": "PKR", "Qatar": "QAR",
        "Ukraine": "UAH", "Peru": "PEN",
        "Vietnam": "VND", "Bangladesh": "BDT",
        "Kenya": "KES", "Norway": "NOK",
        "Iraq": "IQD", "Iran": "IRR",
        "Kuwait": "KWD", "Lebanon": "LBP",
        "Nepal": "NPR", "Oman": "OMR",
        "Sri Lanka": "LKR", "Syria": "SYP",
        "Yemen": "YER", "Zimbabwe": "ZWD",
    }

    
    # Split the data into chunks of 6 elements each
    chunks = [list(currencies.items())[i:i+6] for i in range(0, len(currencies), 6)]

    print("Available currencies for conversion:")
    for chunk in chunks:
        # Pad the chunk with empty strings to ensure each row has 6 elements
        while len(chunk) < 6:
            chunk.append((" ", " "))

        # Transpose the chunk to get a row-wise structure
        transposed_chunk = list(zip(*chunk))
        print(tabulate(transposed_chunk, tablefmt="grid"))
        print()  # Add an empty line between chunks

    # Get source currency input
    while True:
        source_currency = input("Enter source currency: ").upper()
        if source_currency in currencies.values():
            break
        else:
            print("Invalid currency. Please try again.")

    # Get target currency input
    while True:
        target_currency = input("Enter target currency: ").upper()
        if target_currency in currencies.values():
            break
        else:
            print("Invalid currency. Please try again.")

    # Get amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    # Perform currency conversion
    c = CurrencyRates()
    converted_amount = c.convert(source_currency, target_currency, amount)
    print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
