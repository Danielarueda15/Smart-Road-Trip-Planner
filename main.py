# Adding Fuel Calculator

def calculate_fuel_cost():
    miles = float(input("Enter the total trip miles: "))
    mpg = float(input("Enter your vehicle's miles per gallon (MPG): "))
    gas_price = float(input("Enter the current gas price per gallon: "))

    gallons_needed = miles / mpg
    fuel_cost = gallons_needed * gas_price

    print(f"Estimated fuel cost for your trip: ${fuel_cost:.2f}")


# Main Page
def main():
    print("Welcome to the Smart Road Trip Planner- Let's plan your trip!")
    calculate_fuel_cost()

main()