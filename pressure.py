from tabulate import tabulate

def convert_pressure():
    print("Welcome to the Pressure Conversion Tool!")
    
    # Define pressure units
    units = {
        "Millimetre of water (mmw)": "mmw", 
        "Pounds/square foot (psf)": "psf", 
        "Kilogram-force/square centimetre (kfcm)": "kfcm",
        "Pounds/square inch (psi)": "psi",
        "Millimetre of mercury (mmhg)": "mmhg",
        "Bar (b)": "b",
        "Inch of mercury (inhg)": "inhg",
        "Millibar (mbar)": "mbar",
        "Hectopascal (hpa)": "hpa",
        "Standard atmosphere (atm)": "atm",
        "Kilopascal (kpa)": "kpa",
        "Kilogram-force/square metre (kfm)": "kfm",
        "Megapascal (mpa)": "mpa"
    }

    # Display available pressure units for conversion
    print("Available pressure units for conversion:")
    print(tabulate([(key, value) for key, value in units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source pressure unit input
    while True:
        source_pressure = input("\nEnter source pressure unit abbreviation: ").strip().lower()
        if source_pressure in units.values():
            break
        else:
            print("Invalid pressure unit abbreviation. Please try again.")

    # Get target pressure unit input
    while True:
        target_pressure = input("Enter target pressure unit abbreviation: ").strip().lower()
        if target_pressure in units.values():
            break
        else:
            print("Invalid pressure unit abbreviation. Please try again.")

    # Get pressure amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_pressure.upper()} to {target_pressure.upper()}...")

    # Define conversion factors
    conversion_factors = {
        "mmw": 9.80665 / 1000,  # Convert millimeter of water to kilopascal
        "psf": 47.880258888889, # Convert pounds/square foot to pascal
        "kfcm": 98.0665 / 10,   # Convert kilogram-force/square centimeter to kilopascal
        "psi": 6894.75729,      # Convert pounds/square inch to pascal
        "mmhg": 133.322,        # Convert millimeter of mercury to pascal
        "b": 100000,            # Convert bar to pascal
        "inhg": 3386.389,       # Convert inch of mercury to pascal
        "mbar": 100,            # Convert millibar to pascal
        "hpa": 100,             # Hectopascal is equivalent to millibar
        "atm": 101325,          # Convert standard atmosphere to pascal
        "kpa": 1000,            # Kilopascal is equivalent to 1000 pascal
        "kfm": 9.80665 * 1000,  # Convert kilogram-force/square meter to pascal
        "mpa": 1000000          # Convert megapascal to pascal
    }

    # Pressure Conversion Logic
    converted_pressure = amount * conversion_factors[source_pressure] / conversion_factors[target_pressure]
    print(f"{amount} {source_pressure} is equal to {converted_pressure} {target_pressure}")
