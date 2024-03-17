from tabulate import tabulate

def convert_time():
    print("Welcome to the Time Conversion Tool!")

    # Define time units
    units = {
        "Planck time (ps)": "ps", 
        "Yoctosecond (y)": "y", 
        "Zeptosecond (z)": "z", 
        "Attosecond (a)": "a", 
        "Femtosecond (f)": "f", 
        "Picosecond (p)": "p", 
        "Nanosecond (n)": "n", 
        "Microsecond (u)": "u", 
        "Millisecond (m)": "m", 
        "Second (s)": "s", 
        "Minute (min)": "min", 
        "Hour (h)": "h", 
        "Day (d)": "d", 
        "Week (w)": "w", 
        "Month (mo)": "mo", 
        "Quarter (q)": "q", 
        "Year (y)": "year", 
        "Decade (dec)": "dec", 
        "Century (c)": "c", 
        "Millennium (M)": "mil",
    }

    # Display available time units for conversion
    print("Available time units for conversion:")
    print(tabulate([(key, value) for key, value in units.items()], headers=["Unit", "Abbreviation"], tablefmt="grid"))

    # Get source time unit input
    while True:
        source_time = input("\nEnter source time unit abbreviation: ").strip().lower()
        if source_time in units.values():
            break
        else:
            print("Invalid time unit abbreviation. Please try again.")

    # Get target time unit input
    while True:
        target_time = input("Enter target time unit abbreviation: ").strip().lower()
        if target_time in units.values():
            break
        else:
            print("Invalid time unit abbreviation. Please try again.")

    # Get time amount input
    while True:
        try:
            amount = float(input("Enter time amount: ").strip())
            break
        except ValueError:
            print("Invalid time amount. Please enter a valid number.")

    print(f"\nConverting {amount} {source_time.upper()} to {target_time.upper()}...")

    # Define conversion factors
    conversion_factors = {
        "ps": 5.39106e-44,
        "y": 0.000000000000000000000001,
        "z": 0.000000000000000000001,
        "a": 0.000000000000000001,
        "f": 0.000000000000001,
        "p": 0.000000000001,
        "n": 0.000000001,
        "u": 0.000001,
        "m": 0.001,
        "s": 1,
        "min": 60,
        "h": 3600,  
        "d": 86400,  
        "w": 604800,  
        "mo": 2628000,  
        "q": 7884000,  
        "year": 31536000,  # 1 year = 365.25 days (on average, accounting for leap years)
        "dec": 315360000,  
        "c": 3153600000,  
        "mil": 31536000000,  
    }

    # Time Conversion Logic
    converted_time = amount * conversion_factors[source_time] / conversion_factors[target_time]
    print(f"{amount} {source_time.upper()} is equal to {converted_time:.2f} {target_time.upper()}.")

