kosten_bestelling = float(input("Verzendkosten te betalen: "))

if kosten_bestelling >= 50:
    print("Gratis verzending!")
elif kosten_bestelling >= 25:
    print("€3 verzendkosten.")
elif kosten_bestelling < 25:
    print("€5 verzendkosten.")
