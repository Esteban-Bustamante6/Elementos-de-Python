import csv
from login import User_Create_Auto
Archivo_MembersCSV = r"C:\Users\Administrador\Desktop\RIWII\Modle_Riwi\Membership\Members.csv"
datos = []
def load_Csv():
    with open(Archivo_MembersCSV, "r", encoding="latin-1") as archivo:
            lector = csv.DictReader(archivo)
            

            for fila in lector:
                datos.append({
                    "Name": "",
                    "ID":"",
                    "Phone":"",
                    "Email":"",
                    "Date_Init":"",
                    "Date_finis":"",
                    "Status":"",
                    "Plane":""
                })
def load_Member ():
    carga = User_Create_Auto()
    with open(Archivo_MembersCSV, "r", newline="") as archivo2:
        writer = csv.writer(archivo2)
        writer.writerow(["Name","ID","Phone","Email","Date_Init","Date_finis","Status","Plane"])
        for u in carga:
            print(u)
