def calculate_fuel(cargo_weight):
    base_weight = 50000
    total_weight = base_weight + cargo_weight
    fuel_needed = total_weight * 3
    return fuel_needed

total_cargo_weight = 0

while True:
    cargo = input("Enter cargo (satellite, rover, supplies) or 'launch': ").lower()

    if cargo == "launch":
        break

    elif cargo == "satellite":
        total_cargo_weight += 1000
        print("SATELLITE!")

    elif cargo == "rover":
        total_cargo_weight += 2500
        print("ROVER!")

    elif cargo == "supplies":
        total_cargo_weight += 500
        print("SUPPLIES")

    else:
        print("Item not approved")

    if total_cargo_weight > 10000:
        print("MAX WEIGHT REACHED")
        break

fuel = calculate_fuel(total_cargo_weight)

print("Total cargo weight:", total_cargo_weight, "kg")