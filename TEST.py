# Makola Market Inventory and Sales System

inventory ={
    "Tomatoes": {"stock":150, "price_per_unit":5.0},
    "Onions": {"stock": 80, "price_per_unit": 3.5} ,
    "Garden Eggs": {"stock": 200, "price_per_unit": 1.0} 
}
print(inventory)

Transaction_count = []

while True:
    print("1. Tomatoes")
    print("2. Onions")
    print("3. Garden Eggs")
    print("4. exit")

    choice = input("Enter item name to purchase(Tomatoes, Onions,Garden Eggs): ")
    if choice == "exit" :
        print("Closing sales. Total transactions completed")
        break
    elif choice == "Tomatoes" or choice == "Onions" or choice == "Garden Eggs":
        quantity=int(input("Enter quantity to buy: "))

        stock = inventory[choice]["stock"]
        price = inventory[choice]["price_per_unit"]

        if quantity > stock:
            print(f"Sorry, only {stock} units of {choice} remaining")
        else:
            cost = quantity * price
            inventory[choice]["stock"] = stock - quantity
            Transaction_count.append(choice)
            print(f"Sale successful! Cost: GHS{cost:.2f}. {inventory[choice]["stock"]} units of {choice}")
    else:
        print("Item not found in stock. Check spelling")


# Ghana Water Company(GWCL) Bill Calculator

service_charge = 15.00

consumption= float(input("Enter your total water consumption for the month (in cubic meters): "))
consumption_cost = []

if consumption <= 15:
    consumption_cost = consumption * 0.90

elif consumption <=30:
     first_tier = 15 * 0.90
     remainder = consumption - 15
     second_tier = remainder * 1.20
     consumption_cost = first_tier + second_tier



else:
     first_tier = 15 * 0.90
     second_tier = 15 * 1.20
     remainder = consumption - 30
     third_tier = remainder * 1.50
     consumption_cost = first_tier + second_tier + third_tier

total_bill = service_charge + consumption_cost
print("--- Monthly Water Bill Summary ---")
print(f"Consumption: {consumption:.2f} m3")
print(f"Service Charge: GHS {service_charge:.2f}")
print(f"Consumption Cost: GHS {consumption_cost:.2f}")
print(f"Total Bill: GHS {total_bill:.2f}")

# Speed Analysis Script for Ghana Police Service


recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
SPEED_LIMIT = 100

speeding_violations = []

for speed in recorded_speeds:
    if speed > SPEED_LIMIT:
        print(f"WARNING: Vehicle recorded at {speed} km/h. Exceeded limit of {SPEED_LIMIT} km/h.")
        speeding_violations.append(speed)


total_vehicles = len(recorded_speeds)
total_violations = len(speeding_violations)

percentage_of_vehicles_speeding = (total_violations / total_vehicles) * 100


total_speed = 0
for speed in recorded_speeds:
    total_speed += speed

average_speed = total_speed / total_vehicles

print("--- Speed Analysis Summary ---")
print(f"Total vehicles recorded: {total_vehicles}")
print(f"Total speeding violations: {total_violations}")
print(f"Percentage of vehicles speeding: {percentage_speeding:.2f}%")
print(f"Average speed of vehicles: {average_speed:.2f} km/h")

focused_segment = recorded_speeds[2:8]

print("Speeds for focused inspection segment (3rd to 8th vehicle):")
print(focused_segment)
   


