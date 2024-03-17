from currency import convert_currency
from length import convert_length
from area import convert_area
from volume import convert_volume
from weight import convert_weight
from temperature import convert_temperature
from speed import convert_speed
from pressure import convert_pressure
from power import convert_power
from times import convert_time
from data import convert_data

def convert_unit():
    while True:
        print("\nUnit Conversion Menu:")
        print("1. Currency")
        print("2. Length")
        print("3. Area") 
        print("4. Volume")
        print("5. Weight")
        print("6. Temperature")
        print("7. Speed")
        print("8. Pressure")
        print("9. Power")
        print("10. Time")
        print("11. Data Storage")
        print("12. Back to Main Menu")
        amount_choice = input("Enter your choice: ")
        if amount_choice == "1":
            convert_currency()
        elif amount_choice == "2":
            convert_length()
        elif amount_choice == "3":
            convert_area()
        elif amount_choice == "4":
            convert_volume()
        elif amount_choice == "5":
            convert_weight()
        elif amount_choice == "6":
            convert_temperature()
        elif amount_choice == "7":
            convert_speed()
        elif amount_choice == "8":
            convert_pressure()
        elif amount_choice == "9":
            convert_power()
        elif amount_choice == "10":
            convert_time()
        elif amount_choice == "11":
            convert_data()
        elif amount_choice == "12":
            break  # Return to main menu
        else:
            print("Invalid choice. Please try again.")