navn = input("Hva heter du?")

print("hei,", navn)

print(f"Hei, {navn}!")

alder = input("Hvor gammel er du? ")
print(type(alder))


# print(alder + 1) Den var feil, not int

alder = int(alder)
print(type(alder))

print(f"Du blir {alder + 1} neste år")

høyde = input("Hvor høy er du?")
print(høyde)

#høyde = int(høyde)

høyde = float(høyde)
print(type(høyde))




# --- Refleksjon ---
# Når e bruker int så kommer det en feilmelding ValueError: invalid literal for int() with base 10: '1.73'
# E må bruke float istedenfor int fordi float er for decimaltall
# Fikk denne erroren når e ikke hadde skrevet int TypeError: can only concatenate str (not "int") to str
# Python klagde på at de ikke kunne blande datatypene int og str
# Forskjellen er at du bruker komma i den vanlige og ikke komma i f strengen
# Det blir ikke riktig fordi tretti er tekst og 30 er tall, og man må definere de