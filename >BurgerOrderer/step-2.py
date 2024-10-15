def visa_meny():
    menu = {
        "Pommes frites": 25,
        "Lökringar": 30,
        "Kycklingvingar": 50,
        "Mozzarella sticks": 35,
        "Sallad": 20,
    }
    print("Välkommen till tillbehörsmenyn!")
    print("Här är våra tillgängliga tillbehör:\n")
    
    for item, price in menu.items():
        print(f"{item}: {price} kr")

def beställ_tillbehör():
    menu = {
        "Pommes frites": 25,
        "Lökringar": 30,
        "Kycklingvingar": 50,
        "Mozzarella sticks": 35,
        "Sallad": 20
    }
    while True:
        val = input("\nVilket tillbehör vill du beställa? Skriv namnet på tillbehöret: ")
        if val in menu:
            print(f"\nDu har beställt {val}. Det kostar {menu[val]} kr.")
        else:
            print("\nTyvärr, vi har inte det tillbehöret.")
        igen = input("\nVill du beställa något annat? (ja/nej): ")
        if igen.lower() != "ja":
            print("Tack för ditt besök!")
            break

visa_meny()
beställ_tillbehör()

    
