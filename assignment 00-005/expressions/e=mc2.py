# Speed of light constant in meters per second
C = 299_792_458

while True:
    try:
        mass_input = input("\nEnter kilos of mass (or type 'exit' to quit): ")
        
        if mass_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Convert input to float
        m = float(mass_input)

        # Calculate energy using E = m * c^2
        E = m * C**2

        # Display results
        print("\ne = m * C^2...\n")
        print(f"m = {m} kg")
        print(f"C = {C} m/s")
        print(f"{E} joules of energy!")
        
    except ValueError:
        print("Please enter a valid number or type 'exit' to quit.")
