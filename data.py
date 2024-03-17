from tabulate import tabulate

def convert_data():
    print("Welcome to the Data Storage Conversion Tool!")

    # Define data storage units
    units = {
        "Yottabyte (YB)": "yb",
        "Zettabyte (ZB)": "zb",
        "Exabyte (EB)": "eb",
        "Petabyte (PB)": "pb",
        "Terabyte (TB)": "tb",
        "Gigabyte (GB)": "gb",
        "Megabyte (MB)": "mb",
        "Kilobyte (KB)": "kb",
        "Byte (B)": "byte",
        "Bit (b)": "bit",
        "Nibble (n)": "n"
    }

    # Display available data storage units for conversion
    print("Available data storage units for conversion:")
    print(tabulate([(key, value) for key, value in units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source data storage unit input
    while True:
        source_storage = input("\nEnter source data storage unit abbreviation: ").strip().lower()
        if source_storage in units.values():
            break
        else:
            print("Invalid data storage unit abbreviation. Please try again.")

    # Get target data storage unit input
    while True:
        target_storage = input("Enter target data storage unit abbreviation: ").strip().lower()
        if target_storage in units.values():
            break
        else:
            print("Invalid data storage unit abbreviation. Please try again.")

    # Get data storage amount input
    while True:
        amount = input("Enter data storage amount: ").strip()
        if amount.isdigit():
            break
        else:
            print("Invalid data storage amount. Please try again.")

    print(f"\nConverting {amount} {source_storage.upper()} to {target_storage.upper()}...")

    # Define conversion factors
    conversion_factors = {
        "yb": 1e24,
        "zb": 1e21,
        "eb": 1e18,
        "pb": 1e15,
        "tb": 1e12,
        "gb": 1e9,
        "mb": 1e6,
        "kb": 1e3,
        "byte": 1,
        "bit": 0.125,
        "n": 0.5
    }

    # Data Storage Conversion Logic
    converted_storage = float(amount) * conversion_factors[source_storage] / conversion_factors[target_storage]
    print(f"{amount} {source_storage.upper()} is equal to {converted_storage:.2f} {target_storage.upper()}.")
