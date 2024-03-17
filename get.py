def get_integer(message):
    while True:
        key = input(message)
        try:
            key = int(key)  # Convert input to an integer
            return key 
        except ValueError:
            print("Error: Please enter a valid integer.")
    
    