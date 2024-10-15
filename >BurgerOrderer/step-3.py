def visa_meny():
    menu = {
        "Coca-Cola": 20,
        "Pepsi": 18,
        "Fanta": 17,
        "Sprite": 19,
        "Vatten": 10,
    }
    print("Välkommen till drickmenyn!")
    print("Här är våra tillgängliga drycker:\n")
    
    for drink, price in menu.items():
        print(f"{drink}: {price} kr")

def beställ_dryck():
    menu = {
        "Coca-Cola": 20,
        "Pepsi": 18,
        "Fanta": 17,
        "Sprite": 19,
        "Vatten": 10
    }
    while True:
        val = input("\nVilken dryck vill du beställa? Skriv namnet på drycken: ")
        if val in menu:
            print(f"\nDu har beställt {val}. Det kostar {menu[val]} kr.")
        else:
            print("\nTyvärr, vi har inte den drycken.")
        igen = input("\nVill du beställa något annat? (ja/nej): ")
        if igen.lower() != "ja":
            print("Tack för ditt besök!")
            break

visa_meny()
beställ_dryck()
