# Adding Fuel Calculator

def calculate_fuel_cost():
    miles = float(input("Enter the total trip miles: "))
    mpg = float(input("Enter your vehicle's miles per gallon (MPG): "))
    gas_price = float(input("Enter the current gas price per gallon: "))

    gallons_needed = miles / mpg
    fuel_cost = gallons_needed * gas_price

    print(f"Estimated fuel cost for your trip: ${fuel_cost:.2f}")

# Lodging Calculator

def calculate_lodging_cost():
    nights = int(input("Enter the number of nights you'll be staying: "))
    cost_per_night = float(input("Enter the cost per night: "))

    lodging_codst = nights * cost_per_night
    print(f"Estimated lodging cost for your trip: ${lodging_codst:.2f}")  


# Main Page

def main():
    print("Welcome to the Smart Road Trip Planner- Let's plan your trip!")
    calculate_fuel_cost()
    calculate_lodging_cost()

main()