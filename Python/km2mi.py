
name= input('What is your name?: ')
distance_km= input('What is the distance in km?: ')
answer=float(distance_km)/1.609

print(f'Hello {name.title()}! {distance_km}km is equal to {round(answer,1)} miles' )