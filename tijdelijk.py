def print_aanbieding():
    # Aanmaken van een dictionary voor prijzen ijs-smaken
    prijzen = {
        "aardbei" : 3,
        "vanille" : 4,
        "chocolade" : 5
    }

    # Aanbieding berekenen voor aardbei-ijs
    aanbieding = prijzen["aardbei"] * 0.8

    # Reclame-tekst maken (en bedrag afronden)
    reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding}"
    reclame_tekst2 = reclame_tekst[:62]

    # Een variant van de reclame-tekst in hoofdletters
    reclame_tekst3 = reclame_tekst2.upper()

    # Een lijst maken van de reclame-tekst
    reclame_tekst4 = reclame_tekst3.split(" ")

    # De reclame-tekst afdrukken, woorden onder elkaar
    for el in reclame_tekst4:
        if len(el) >= 5:
            print(el)
        else:
            print(el.lower())

print_aanbieding()