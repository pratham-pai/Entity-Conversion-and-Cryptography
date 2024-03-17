from tabulate import tabulate

def convert_weight():
    print("Welcome to the Weight Conversion Tool!")
    
    # Metric weight units
    metric_units = {
        "Gram (g)": "g", 
        "Microgram (µg)": "ug", 
        "Quintal (q)": "q", 
        "Carat (ct)": "ct", 
        "Tonne (t)": "ton", 
        "Milligram (mg)": "mg", 
        "Kilogram (kg)": "kg"
    }
    
    # Imperial weight units
    imperial_units = {
        "Short ton (st)": "st", 
        "Long ton (lt)": "lt", 
        "Ounce (oz)": "oz", 
        "Grain (gr)": "gr", 
        "Dram (dr)": "dr", 
        "Pound (lb)": "lb", 
        "Stone (sto)": "sto"
    }

    # Display available weight units for conversion
    print("Available weight units for conversion (Metric System):")
    print(tabulate([(key, value) for key, value in metric_units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))
    print("\nAvailable weight units for conversion (Imperial System):")
    print(tabulate([(key, value) for key, value in imperial_units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source weight unit input
    while True:
        source_weight = input("\nEnter source weight unit abbreviation: ").strip().lower()
        if source_weight in metric_units.values() or source_weight in imperial_units.values():
            break
        else:
            print("Invalid weight unit abbreviation. Please try again.")

    # Get target weight unit input
    while True:
        target_weight = input("Enter target weight unit abbreviation: ").strip().lower()
        if target_weight in metric_units.values() or target_weight in imperial_units.values():
            break
        else:
            print("Invalid weight unit abbreviation. Please try again.")

    # Get amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_weight.upper()} to {target_weight.upper()}...")
    
    # Conversion factors
    conversion_factors = {
        # Metric units
        "g": 1,         # Gram
        "ug": 0.000001, # Microgram
        "q": 100000,    # Quintal
        "ct": 0.0002,   # Carat
        "ton": 1000000, # Tonne
        "mg": 0.001,    # Milligram
        "kg": 1000,      # Kilogram
        # Imperial units
        "st": 0.00000110231131,  # Short ton
        "lt": 0.000000984206527, # Long ton
        "oz": 0.0352739619,      # Ounce
        "gr": 15.432358529,      # Grain
        "dr": 0.5643833912,      # Dram
        "lb": 0.0022046226,      # Pound
        "sto": 0.000157473       # Stone
    }

    # Weight Conversion Logic
    converted_weight = amount * conversion_factors[source_weight] / conversion_factors[target_weight]
    print(f"{amount} {source_weight} is equal to {converted_weight} {target_weight}")
