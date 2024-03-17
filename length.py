from tabulate import tabulate

def convert_length():
    print("Welcome to the Length Conversion Tool!")
    # Metric length units
    metric_units = {
        "Decimeter (dm)": "dm", "Lightyear (ly)": "ly", "Millimeter (mm)": "mm",
        "Kilometer (km)": "km", "Centimeter (cm)": "cm", "Metre (m)": "m",
        "Micrometer (um)": "um", "Parsec (pc)": "pc", "Astronomical unit (au)": "au",
        "Picometer (pm)": "pm", "Nanometer (nm)": "nm"
    }

    # Imperial length units
    imperial_units = {
        "Furlong (fur)": "fur", "Yard (yd)": "yd", "Nautical mile (nmi)": "nmi",
        "Foot (ft)": "ft", "Mile (mi)": "mi", "Inch (in)": "in"
    }

    # Display available length units for conversion
    print("Available length units for conversion (Metric System):")
    print(tabulate([(key, value) for key, value in metric_units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))
    print("\nAvailable length units for conversion (Imperial System):")
    print(tabulate([(key, value) for key, value in imperial_units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source length unit input
    while True:
        source_length = input("\nEnter source length unit abbreviation: ").strip().lower()
        if source_length in metric_units.values() or source_length in imperial_units.values():
            break
        else:
            print("Invalid length unit abbreviation. Please try again.")

    # Get target length unit input
    while True:
        target_length = input("Enter target length unit abbreviation: ").strip().lower()
        if target_length in metric_units.values() or target_length in imperial_units.values():
            break
        else:
            print("Invalid length unit abbreviation. Please try again.")

    # Get amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_length.upper()} to {target_length.upper()}...")
    # Define conversion factors
    conversion_factors = {
        # Metric units
        "dm": 0.1, "ly": 9.461e+15, "mm": 0.001,
        "km": 1000, "cm": 0.01, "m": 1,
        "um": 1e-6, "pc": 3.086e+16, "au": 1.496e+11,
        "pm": 1e-12, "nm": 1e-9, 
        # Imperial units
        "fur": 201.168, "yd": 0.9144, "nmi": 1852,
        "ft": 0.3048, "mi": 1609.34, "in": 0.0254
    }

    # Length Conversion Logic
    converted_length = amount * conversion_factors[source_length] / conversion_factors[target_length]
    print(f"{amount} {source_length} is equal to {converted_length} {target_length}")
