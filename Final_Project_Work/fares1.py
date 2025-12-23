def fare(base_fare, luggage_weight):
    Extra_charge = 0
     
    
    if luggage_weight > 20:
        Extra_charge = (luggage_weight - 20) * 2.5  #Gh₵2.5 per extra kg
        
    return base_fare + Extra_charge

