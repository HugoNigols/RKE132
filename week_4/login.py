

#meie ülesanne on luua lihtne vorm kasutaja andmete kontrollimiseks – nimelt kasutajanime ja parooli kontroll.

username = input("Sisesta kasutajanimi:")
password = input("Sisesta parool:")

#or
if username != "user" or password != "1234":
    print("Access denied")
else:
    print("Welcome")


# if username == "user":
#     if password == "1234":
#         print("Welcome!")
#     else:
#         print("Access denied!")
# else:
#     print("Access denied!")

    
#     #and

#     if username == "user" and password == "1234":
#         print("Welcome!")
#     else:
#         print("Access denied!")
