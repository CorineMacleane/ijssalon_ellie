from algemene_functies import mijn_functie_2

# Opgave 5: Reclame-tekst maken voor aanbieding
def aanbieding_1(smaak, prijs, korting):
    nieuwe_prijs = prijs - korting * prijs
    return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {nieuwe_prijs:.2f} euro."

# Opgave 6/7: Totale inkomsten en btw berekenen.
def inkomsten_totaal(inkomsten, btw=0.0):
    totaal = sum(inkomsten)
    te_betalen = btw * totaal
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {te_betalen:.2f} euro btw betaald dient te worden."

# Opgave 8: Hoogste en laagste waarde in lijst vinden en teruggeven als lijst
def hoog_en_laag(mijn_lijst):
    return [max(mijn_lijst), min(mijn_lijst)]

# Opgave 9/10: De gemiddelde inkomsten berekenen en in bericht teruggeven
def gemiddelde(mijn_lijst):
    gemiddelde_inkomsten = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten van deze week zijn {gemiddelde_inkomsten:.2f} euro."

# Opgave 11: Nog eens de hoogste en laagste waarde teruggeven (functie hoog_en_laag hergebruiken)
def meervoudig(invoer_lijst):
    return hoog_en_laag(invoer_lijst)

# Opgave 12: (Bovenaan code wordt functie geimporteerd)
def combinatie(invoer_lijst_2):
    korte_lijst = hoog_en_laag(invoer_lijst_2)
    return mijn_functie_2(korte_lijst[0], korte_lijst[1])


