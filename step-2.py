from flask import Flask, render_template, request, redirect, url_for
import request

"""
    Visar tillbehörsmenyn med tillgängliga alternativ och deras priser.

    Funktionen skriver ut en lista över tillbehör tillsammans med
    respektive priser för att informera användaren om vad som
    kan beställas.
    """

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
      

    """
    Hanterar beställningar av tillbehör.
    """

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

    if __name__ == "__main__":

