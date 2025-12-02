from login import *
from member import *

activite = True
while activite:
    option = int(input("______________Main Mennu_______________\n(1) Login\n(2) Members\n(3) Asistation\n(4) Page\n(5) Report\n(6) Exit\n Put the number for Option : "))
    until= 6
    if option <= 0 :
        print("Eror date negative")
        continue
    elif option == 1:
        User_Create_Auto()
        Load_User_Csv()
        cargarCSV()
        Validacion()

        print("register")
    elif option == 2:
        load_Csv()
        load_Member()
        print("memb")
    elif option == 3:
        print("asiste")

    elif option > until:
        print("date not valide , out the range")
        continue
    if option == 6:
        print("Exit")
        break