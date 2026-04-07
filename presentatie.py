def presenteer(mijn_dict, totaal):
    print()
    for sleutel in mijn_dict:
        print(sleutel + " : " + str(mijn_dict[sleutel]) + " euro")
    print(26 * "=")
    print("Totaal : " + str(totaal) + " euro")