from models1 import Passenger   #Importing Necessary Clssses and Functions
import fares1 as f
import time
import utils1 as u


def get_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("This field is required. Please enter a value.")
        else:
            return value
Bus_Capacity = 45
Base_Fare = 180
Passengers = []
while True:
    print("="*60)
    print("          GPRTU Digital Manifest & Fare System ")
    print("                     Accra - Kumsasi")
    print("               Smart Records, Smooth Journeys")
    print("="*60)
    print("1. Book Ticket")
    print("2. View VIP List")
    print("3. View Passenger list")
    print("4. Exit")
    
    choice = input("Enter Your Choice: ").lower()
    if choice == '1' or choice == 'book ticket':
        if len(Passengers) >= Bus_Capacity:
            print("\n--Bus is full kindly wait for the next bus")
            time.sleep(2)
            continue
        name = get_input("Enter passenger name: ")
        seat_number = len(Passengers) + 1
        Next_of_Kin = get_input("Next of Kin: ")
        luggage_weight = float(input("Enter Luggage weight(kg): "))
        if luggage_weight < 0:
            print("Luggage weight cannot be negative")
            input("\nPress Enter to continue...")
            time.sleep(1)
            continue

        fare = f.fare(Base_Fare, luggage_weight)
        passenger = Passenger(name,seat_number,Next_of_Kin)
        Passengers.append(passenger)
        print(f"Ticket booked successfully for {name}. Seat Number: {seat_number}. Total Fare: Gh₵{fare}")
        input("\nPress Enter to continue...")
        time.sleep(1)
    elif choice == '2' or choice == 'view vip list':
        if len(Passengers) == 0:
            print("\nNo VIP Passengers have been booked yet.")
            print("Book now to become a VIP Passenger!")
            input("\nPress Enter to continue...")
            time.sleep(1)
        else:
            u.VIP_List(Passengers)  
            input("\nPress Enter to continue...")
            time.sleep(1)

    elif choice == '3' or choice == 'view passenger list':

        if len(Passengers) == 0:
            print("\nNo Passengers have been booked yet.")
            input("\nPress Enter to continue...")
            time.sleep(1)
           
        else:
            u.Passenger_List(Passengers)
            input("\nPress Enter to continue...")
            time.sleep(1)

    elif choice == '4' or choice == 'exit':
        print("Thank you for working with us!")
        break
    else:
        print("Invalid option.")


