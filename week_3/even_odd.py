
#Programm palub kasutajal sisestada arvu. Kasutaja sisestab arvu. 
#Programm määrab, kas arv on paaris või paaritu, ja annab vastava tagasiside.

#Modulus (%)



n = int(input("Sisesta täisarv:"))

# if n % 2 == 0:
#     print("Arv on paaris")
# else:
#     print("Arv on paaritu")

# #ternary operator
# print("Arv on paaris" if n % 2 == 0 else "Arv on paaritu")

match n % 2:
    case 0:
        print("Arv on paaris")
    case _:
        print("Arv on paaritu")
      
