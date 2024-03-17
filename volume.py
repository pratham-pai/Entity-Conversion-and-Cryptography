from tabulate import tabulate
from keyboard_cube import print_keyboard_instructions

def convert_volume():
    print("Welcome to the Volume Conversion Tool!")
    # Metric volume units
    metric_units = {
        "Hectolitre (hl)": "hl", "Cubic metre (m³)": "m³", "Cubic centimetre (cm³)": "cm³",
        "Decilitre (dl)": "dl", "Centilitre (cl)": "cl", "Cubic decimetre (dm³)": "dm³",
        "Litre (l)": "l", "Cubic millimetre (mm³)": "mm³", "Millilitre (ml)": "ml"
    }

    # Imperial volume units
    imperial_units = {
        "Cubic foot (ft³)": "ft³", "US fluid ounce (US fl oz)": "usfloz", "Cubic yard (yd³)": "yd³",
        "Cubic inch (in³)": "in³", "Acre-foot (af)": "af", "UK gallon (UK gal)": "ukgal",
        "US gallon (US gal)": "usgal", "UK fluid ounce (UK fl oz)": "ukfloz"
    }

    # Let the user know how to type "³" for the abbreviations ahead
    choice = input("Do you want instructions on how to type '³'? (yes/no)").lower()

    while choice not in ['yes', 'no']:
        print("Invalid choice, please enter 'yes' or 'no'")
        choice = input("Do you want instructions on how to type '³'? (yes/no)").lower()

    if choice == "yes":
        print_keyboard_instructions()
    else:
        print("No instructions provided.")

    # Display available volume units for conversion
    print("Available volume units for conversion (Metric System):")
    print(tabulate([(key, value) for key, value in metric_units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))
    print("\nAvailable volume units for conversion (Imperial System):")
    print(tabulate([(key, value) for key, value in imperial_units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source volume unit input
    while True:
        source_volume = input("\nEnter source volume unit abbreviation: ").strip().lower()
        if source_volume in metric_units.values() or source_volume in imperial_units.values():
            break
        else:
            print("Invalid volume unit abbreviation. Please try again.")

    # Get target volume unit input
    while True:
        target_volume = input("Enter target volume unit abbreviation: ").strip().lower()
        if target_volume in metric_units.values() or target_volume in imperial_units.values():
            break
        else:
            print("Invalid volume unit abbreviation. Please try again.")

    # Get amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_volume.upper()} to {target_volume.upper()}...")
    
    # Define conversion factors
    conversion_factors = {
        # Metric units
        "hl": 100, "m³": 1000, "cm³": 0.001,
        "dl": 0.1, "cl": 0.01, "dm³": 1,
        "l": 1, "mm³": 1e-6, "ml": 0.001,
        # Imperial units
        "ft³": 28.3168, "usfloz": 0.0295735, "yd³": 764.555,
        "in³": 0.0163871, "af": 1233.48, "ukgal": 4.54609,
        "usgal": 3.78541, "ukfloz": 0.0284131
    }

    # Volume Conversion Logic
    converted_volume = amount * conversion_factors[source_volume] / conversion_factors[target_volume]
    print(f"{amount} {source_volume} is equal to {converted_volume} {target_volume}")
