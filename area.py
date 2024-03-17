from tabulate import tabulate
from keyboard_square import print_keyboard_instructions

def convert_area():
    print("Welcome to the Area Conversion Tool!")
    # Metric area units
    metric_units = {
        "Square metre (m²)": "m²", "Square decimetre (dm²)": "dm²", "Square centimetre (cm²)": "cm²",
        "Square kilometre (km²)": "km²", "Square millimetre (mm²)": "mm²", "Are (ar)": "ar",
        "Hectare (ha)": "ha"
    }

    # Imperial area units
    imperial_units = {
        "Square mile (mi²)": "mi²", "Square rod (rd²)": "rd²", "Square yard (yd²)": "yd²",
        "Square foot (ft²)": "ft²", "Acre (ac)": "ac", "Square inch (in²)": "in²"
    }

    # Let the user know how to type "²" for the abbreviations ahead
    choice = input("Do you want instructions on how to type '²'? (yes/no)").lower()

    while choice not in ['yes', 'no']:
        print("Invalid choice, please enter 'yes' or 'no'")
        choice = input("Do you want instructions on how to type '²'? (yes/no)").lower()

    if choice == "yes":
        print_keyboard_instructions()
    else:
        print("No instructions provided.")

    # Display available area units for conversion
    print("Available area units for conversion (Metric System):")
    print(tabulate([(key, value) for key, value in metric_units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))
    print("\nAvailable area units for conversion (Imperial System):")
    print(tabulate([(key, value) for key, value in imperial_units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source area unit input
    while True:
        source_area = input("\nEnter source area unit abbreviation: ").strip().lower()
        if source_area in metric_units.values() or source_area in imperial_units.values():
            break
        else:
            print("Invalid area unit abbreviation. Please try again.")

    # Get target area unit input
    while True:
        target_area = input("Enter target area unit abbreviation: ").strip().lower()
        if target_area in metric_units.values() or target_area in imperial_units.values():
            break
        else:
            print("Invalid area unit abbreviation. Please try again.")

    # Get amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_area.upper()} to {target_area.upper()}...")
    
    # Define conversion factors
    conversion_factors = {
        # Metric units
        "m²": 1, "dm²": 0.01, "cm²": 0.0001,
        "km²": 1000000, "mm²": 0.000001, "ar": 100,
        "ha": 10000, 
        # Imperial units
        "mi²": 2589988.11, 
        "rd²": 25.2929, "yd²": 0.836127,
        "ft²": 0.092903, "ac": 4046.86, "in²": 0.00064516
    }

    # Area Conversion Logic
    converted_area = amount * conversion_factors[source_area] / conversion_factors[target_area]
    print(f"{amount} {source_area} is equal to {converted_area} {target_area}")