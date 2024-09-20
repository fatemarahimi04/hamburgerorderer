class Tillbehör:
    def __init__(self, tillbehör_namn, tillbehör_pris):
        self.namn = tillbehör_namn
        self.pris = tillbehör_pris

    def __str__(self):
        return f"{self.namn}: {self.pris} kr"
  
tillbehörsmeny = [
    Tillbehör("Pommes frites", 30),
    Tillbehör("Sallad", 35),
    Tillbehör("Lökringar", 25),
    Tillbehör("Vitlöksbröd", 30),
    Tillbehör("Mozzarella sticks", 45),
    Tillbehör("Coleslaw", 25)
]

for tillbehör in tillbehörsmeny:
    print(tillbehör)
