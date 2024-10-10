from flask import Flask, render_template, request, redirect, url_for
import request

app = Flask(__name__)

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

@app.route('/')
def visa_meny():
    return render_template('meny.html', burgare_meny=burgare_meny)

@app.route('/bestall/<burger>', methods=['GET', 'POST'])
def beställ_burgare(burger):
    if request.method == 'POST':
        borttagna_ingredienser = request.form.getlist('borttagna')
        kvarvarande_ingredienser = [ing for ing in burgare_meny[burger]['ingredienser] if ing not in borttagna_ingredienser]

        skicka_till_kitchenview(burger, kvarvarande_ingredienser, borttagna_ingredienser)
        return redirect(url_for('tack'))

    return render_template('bestall.html', burger=burger, ingredienser=burgare_meny[burger]['ingredienser'])

def tack():
    return "Tack för din beställning!"

def skick_till_kitchenview(burger, ingredienser, borttagna_ingredienser):
    url = f"http://localhost:500/buy/{burger}"

    params = {
        'kvarvarande': ingredienser,
        'borttagna': borttagna_ingredienser
    }

    respons = request.get(url, params=params)
    print(respons.text)

if __name__ == '__main__':
    app.run(debug=True)
    
def skicka_till_kitchenview(burger, ingredienser, borttagna_ingredienser):
    url = f"http://localhost:5000/buy/{burgare}"

    params = {
        'kvarvarande': ingredienser, 
        'borttagna': borttagna_ingredienser
    }

    respons = requests.get(url, params=params)
    print(respons.text)

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
            
    print(f"\nDin slutgiltiga burgare innehåller: {', '.join(ingredienser)}.")
    if borttagna_ingredienser:
        print(f"Du har tagit bort: {', '.join(borttagna_ingredienser)}.\n")

visa_meny()
beställ_burgare()

        
    
            


  
