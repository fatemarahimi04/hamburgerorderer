burgare_meny = {
    "DemureChicken": {
        "pris": 40,
        "ingredienser": ["kyckling", "sallad", "tomat", "majonnäs"]
    },
    "HeroBurger": {
        "pris": 60,
        "ingredienser": ["nöttkött", "ost", "lök", "sallad", "tomat", "senap"]
    },
    "CutieVeggie": {
        "pris": 50,
        "ingredienser": ["vegetariskt kött", "ost", "sallad", "lök", "tomat", "avokado"]
    }
}

def visa_meny():
    print("Varmt välkommen till menyn, här kan du välja hamburgare och i kommande steg väljer du tillbehör och dricka!")
    print("Dessa burgare har vi idag:\n")
   
    for burger, info in burgare_meny.items():
        print(f"{burger}: {info['pris']} kr")
        print(f"Innehåll: {', '.join(info['ingredienser'])}\n")

def beställ_burgare():
    while True: 
        val = input("\nVilken burgare är du sugen på idag? Ange namn(eller 'avsluta' för att avsluta): ")
        
        if val == "avsluta":
            print("Tack för ditt besök!")
            break
            
        if val in burgare_meny:
            burgare = burgare_meny[val]
            print(f"\nDu har valt {val}. Det kostar {burgare['pris']} kr.")
            print(f"Ingredienser: {', '.join(burgare['ingredienser'])}")
            
            ta_bort_ingredienserna(burgare['ingredienser'])
        else:
            print("Ogiltigt val, försök igen.")

def ta_bort_ingredienser(ingredienser): 
    borttagna_ingredienser = []
    while True:
        val = input(f"\nVill du ta bort någon ingrediens? (skriv namnet eller 'klar' för att fortsätta): ")
        
        if val == "klar":
            break
            
        if val in ingredienser:
            ingredienser.remove(val)
            borttagna_ingredienser.append(val)
            print(f"{val} har tagits bort.")
        else:
            print("Den ingrediensen finns inte på burgaren.")
            
    print(f"\nDin slutgiltiga burgare innehåller: {', '.join(ingrediensier)}.")
    if borttagna_ingredienser:
        print(f"Du har tagit bort: {', '.join(borttagna_ingredienser)}.\n")

visa_meny()
beställ_burgare()

        
    
            


  
