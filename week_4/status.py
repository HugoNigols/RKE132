
# Kirjuta Pythoni programm, mis kontrollib kliendi staatust tema kulutuste põhjal.
# Tingimused:
# Kui klient on kulutanud vähemalt 5000 €, siis tema staatus on Platinum.
# Kui klient on kulutanud vähemalt 1000 €, siis staatus on Gold.
# Kui klient on kulutanud vähemalt 500 €, siis staatus on Silver.
# Kui klient on kulutanud vähemalt 100 €, siis staatus on Bronze.
# Kui vähem kui 100 €, siis on ta Tavaline klient.


spent = int(input("Kui palju raha sa meie juures kulutasid?"))

# if spent >= 5000:
#     print("platinum")
# elif spent >= 1000:
#     print("Gold")
# elif spent >= 500:
#     print("silver")
# elif spent >= 100:
#     print("Bronze")
# else: 
#     print("Regular customer")


if spent < 100:
    print("Regular customer")
elif spent >= 100 and spent < 500:
    print("Bronze")
elif spent >=500 and spent < 1000:
    print("Silver")
elif spent >= 1000 and spent < 5000:
    print("Gold")
else:
    print("Platinum")
