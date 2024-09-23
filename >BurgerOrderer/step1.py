def visa_meny():
    menu = {
        "1) DemureChicken": 40,
        "2) HeroBurger": 60,
        "3) CutieVeggie": 50
    }
    print("Varmt välkommen till burgarmenyn!")
    print("Dessa burgare har vi idag:\n")

    for burger, price in menu.items():
        print(f"{burger}: {price} kr")

def beställ_burgare():
    menu = {
        "1) DemureChicken": 40,
        "2) HeroBurger": 60,
        "3) CutieVeggie": 40
    }
    while True:
        val = input("\nVilken burgare är du sugen på idag? Ange numret: ")
        if val in menu:
            print(f"\nDu har beställt {val}. Det kostar {menu[val]} kr.")

    
  
  
