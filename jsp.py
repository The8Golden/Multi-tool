import math
import platform
import os
import platform
import time


def Clean():
    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")

nombre1 = input("Choisit une fonction (regarde dans le readmy) : ")
test = 0
if nombre1 == "jsp":
    print("jsp")
elif nombre1 == "apprendre le python":
    print("Va sur cette playlist : https://www.youtube.com/playlist?list=PLrSOXFDHBtfHg8fWBd7sKPxEmahwyVBkC")
elif nombre1 == "test":
    while test < 100:
        print("je test")
        test += 1
elif nombre1 == "apprendre le c++":
    print("Tient regarde ces tuto la :)")
    print("https://www.youtube.com/watch?v=hXJu1UADNr8")
    time.sleep(5)
    Clean()
elif nombre1 == "internet":
    os.system("ipconfig")