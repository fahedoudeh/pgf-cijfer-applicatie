# maak een lijst met tuples
studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2),
("Diana", 9.1)]
# print studenten en cifers
print("Studenten en hun cijfers: ")

for naam, cijfer in studenten:
    print(f"{naam} - {cijfer}")

# totaal score optellen

totaal_score = 0

for naam, cijfer in studenten:
    totaal_score += cijfer

# aantal studenten optellen
aantal_studenten = 0
for student in studenten:
    aantal_studenten += 1

# gemiddelde score
gemiddelde_score = totaal_score / aantal_studenten    

# total_score = studenten[0][1] + studenten[1][1] + studenten[2][1] +studenten[3][1]
# total_studanten = len(studenten)
# gemiddelde_score = total_score / total_studanten

print(f"Gemiddelde score is: {gemiddelde_score:.1f}")  

# bepalen best student

beste_naam = studenten[0][0]
beste_cijfer = studenten[0][1]

for naam, cijfer in studenten:
    if cijfer > beste_cijfer:
        beste_naam = naam
        beste_cijfer = cijfer
        
print(f"De beste student in {beste_naam} met een {beste_cijfer}")        
