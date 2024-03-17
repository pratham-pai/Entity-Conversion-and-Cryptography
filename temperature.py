from tabulate import tabulate

def convert_temperature():
    print("Welcome to the Temperature Conversion Tool!")
    # Temperature units
    units = {
        "Degree Rankine (°R)": "r", 
        "Degree Celsius (°C)": "c", 
        "Degree Reaumur (°Re)": "re",
        "Degree Fahrenheit (°F)": "f", 
        "Kelvin (K)": "k"
    }

    # Display available temperature units for conversion
    print("Available temperature units for conversion:")
    print(tabulate([(key, value) for key, value in units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source temperature unit input
    while True:
        source_temperature = input("\nEnter source temperature unit abbreviation: ").strip().lower()
        if source_temperature in units.values():
            break
        else:
            print("Invalid temperature unit abbreviation. Please try again.")
    
    # Get target temperature unit input
    while True:
        target_temperature = input("Enter target temperature unit abbreviation: ").strip().lower()
        if target_temperature in units.values():
            break
        else:
            print("Invalid temperature unit abbreviation. Please try again.")
    
    # Get amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_temperature.upper()} to {target_temperature.upper()}...")
    
    # Conversion logic
    if source_temperature == "c":
        if target_temperature == "c":
            converted_temperature = amount
        elif target_temperature == "f":
            converted_temperature = (amount * 9/5) + 32
        elif target_temperature == "k":
            converted_temperature = amount + 273.15
        elif target_temperature == "r":
            converted_temperature = (amount + 273.15) * 9/5
        elif target_temperature == "re":
            converted_temperature = amount * 4/5
    elif source_temperature == "f":
        if target_temperature == "c":
            converted_temperature = (amount - 32) * 5/9
        elif target_temperature == "f":
            converted_temperature = amount
        elif target_temperature == "k":
            converted_temperature = (amount + 459.67) * 5/9
        elif target_temperature == "r":
            converted_temperature = amount + 459.67
        elif target_temperature == "re":
            converted_temperature = (amount - 32) * 4/9
    elif source_temperature == "k":
        if target_temperature == "c":
            converted_temperature = amount - 273.15
        elif target_temperature == "f":
            converted_temperature = (amount * 9/5) - 459.67
        elif target_temperature == "k":
            converted_temperature = amount
        elif target_temperature == "r":
            converted_temperature = amount * 9/5
        elif target_temperature == "re":
            converted_temperature = (amount - 273.15) * 4/5
    elif source_temperature == "r":
        if target_temperature == "c":
            converted_temperature = (amount - 491.67) * 5/9
        elif target_temperature == "f":
            converted_temperature = amount - 459.67
        elif target_temperature == "k":
            converted_temperature = amount * 5/9
        elif target_temperature == "r":
            converted_temperature = amount
        elif target_temperature == "re":
            converted_temperature = (amount - 491.67) * 4/9
    elif source_temperature == "re":
        if target_temperature == "c":
            converted_temperature = amount * 5/4
        elif target_temperature == "f":
            converted_temperature = amount * 9/4 + 32
        elif target_temperature == "k":
            converted_temperature = amount * 5/4 + 273.15
        elif target_temperature == "r":
            converted_temperature = amount * 9/4 + 491.67
        elif target_temperature == "re":
            converted_temperature = amount

    print(f"{amount} {source_temperature.upper()} is equal to {converted_temperature:.2f} {target_temperature.upper()}.")

