from tabulate import tabulate

def convert_speed():
    print("Welcome to the Speed Conversion Tool!")
    
    # Speed units
    units = {
        "Speed of Light (c)": "c", 
        "Kilometre/second (km/s)": "km/s", 
        "Mile/hour (mph)": "mph",
        "Mach (Ma)": "ma", 
        "Inch/second (in/s)": "in/s", 
        "Metre/second (m/s)": "m/s",
        "Kilometre/hour (km/h)": "km/h"
    }

    # Display available speed units for conversion
    print("Available speed units for conversion:")
    print(tabulate([(key, value) for key, value in units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source speed unit input
    while True:
        source_speed = input("\nEnter source speed unit abbreviation: ").strip().lower()
        if source_speed in units.values():
            break
        else:
            print("Invalid speed unit abbreviation. Please try again.")

    # Get target speed unit input
    while True:
        target_speed = input("Enter target speed unit abbreviation: ").strip().lower()
        if target_speed in units.values():
            break
        else:
            print("Invalid speed unit abbreviation. Please try again.")

    # Get amount input
    while True:
        amount_str = input("Enter the amount to convert: ")
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_speed.upper()} to {target_speed.upper()}...")
    
    # Define conversion factors
    conversion_factors = {
        "c": 299792458,     # Speed of Light in meters per second
        "km/s": 1000,       # Kilometre per second to meter per second
        "mph": 0.44704,     # Mile per hour to meter per second
        "ma": 343,          # Mach to meter per second
        "in/s": 0.0254,     # Inch per second to meter per second
        "m/s": 1,           # Meter per second
        "km/h": 0.277778    # Kilometre per hour to meter per second
    }

    # Speed Conversion Logic
    converted_speed = amount * conversion_factors[source_speed] / conversion_factors[target_speed]
    print(f"{amount} {source_speed} is equal to {converted_speed} {target_speed}")

    # Define maximum allowable speeds for each target speed unit
    max_speeds = {
        "c": 1,  # Speed of light (m/s)
        "km/s": 299792.458,  # Kilometer per second (km/s)
        "mph": 670616629.4,  # Mile per hour (mph)
        "ma": 880991.09,  # Mach (Ma)
        "in/s": 11803149437.00787,  # Inch per second (in/s)
        "m/s": 299792458,  # Meter per second (m/s)
        "km/h": 1079252848.8  # Kilometer per hour (km/h)
    }

    # Give warning message if the converted speed exceeds the maximum allowable speed
    if target_speed in max_speeds and converted_speed > max_speeds[target_speed]:
        print(f"Warning: The calculated speed exceeds the maximum allowable speed of {max_speeds[target_speed]} {target_speed}. This speed is not physically possible.")
