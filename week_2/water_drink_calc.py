glasses_drunk = int(input('Kui palju klaase vett sa juba joonud oled?: '))
percentage = glasses_drunk / 8

if percentage > 1:
    print('Suurepärane, oled oma päevase eesmärgi täitnud!')
elif percentage < 0.5:
    print('Joo rohkem vett, keha vajab seda!')
else:
    print('Tubli, jätka samas vaimus!')