class Passenger:
    def __init__(self, name, seat_number, Next_of_Kin):
         self.name = name
         self.seat_number = seat_number
         self.Next_of_Kin = Next_of_Kin

    def __str__(self):
         return f"{self.name} | Seat:{self.seat_number} | Next of Kin: {self.Next_of_Kin}"

        
    
