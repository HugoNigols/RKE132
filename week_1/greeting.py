last_name = input('sisestage oma perekonnanimi: ')
gender = input('valige enda sugu (m või n): ')

if gender == 'n':
    print(f"Tere, proua {last_name}!")
elif gender == 'm':
    print(f"Tere, härra {last_name}!")
else:
    print(f"Tere tulemast, {last_name}!")