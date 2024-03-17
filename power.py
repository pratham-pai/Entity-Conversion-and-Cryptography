from tabulate import tabulate

def convert_power():
    print("Welcome to the Power Conversion Tool!")
    
    # Define power units
    units = {
        "Joule/second (j/s)": "j/s", 
        "British thermal unit/second (btu/s)": "btu/s", 
        "Metric horsepower (ps)": "ps",
        "Kilogram-metre/second (kgm/s)": "kgm/s",
        "Kilocalorie/second (kcal/s)": "kcal/s",
        "Watt (w)": "w",
        "Imperial horsepower (hp)": "hp",
        "Foot-pound/second (ftlb/s)": "ftlb/s",
        "Newton-metre/second (nm/s)": "nm/s",
        "Kilowatt (kw)": "kw"
    }

    # Display available power units for conversion
    print("Available power units for conversion:")
    print(tabulate([(key, value) for key, value in units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source power unit input
    while True:
        source_power = input("\nEnter source power unit abbreviation: ").strip().lower()
        if source_power in units.values():
            break
        else:
            print("Invalid power unit abbreviation. Please try again.")
    
    # Get target power unit input
    while True:
        target_power = input("Enter target power unit abbreviation: ").strip().lower()
        if target_power in units.values():
            break
        else:
            print("Invalid power unit abbreviation. Please try again.")

    # Get power amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_power.upper()} to {target_power.upper()}...")

    conversion_factors = {
        "j/s": 1,
        "btu/s": 1055.05585262,
        "ps": 735.49875,
        "kgm/s": 9.80665,
        "kcal/s": 4184,
        "w": 1,
        "hp": 745.7,
        "ftlb/s": 1.3558179483314004,
        "nm/s": 0.001,
        "kw": 1000
    }

    # Power Conversion Logic
    converted_power = amount * conversion_factors[source_power] / conversion_factors[target_power]
    print(f"{amount} {source_power} is equal to {converted_power} {target_power}")