import time
from tkinter import *
import colorama
from colorama import Fore , Back , Style
colorama.init(autoreset=True)
root = Tk()
root.title("DOĞUM GÜNÜ HEDİYESİ")
root.geometry("250x250")

def bday():
    time.sleep(0.75)
    print(Fore.LIGHTRED_EX + "                               ~~")
    time.sleep(0.75)
    print(Fore.LIGHTBLACK_EX + "                               | |")
    time.sleep(0.75)
    print(Fore.LIGHTBLACK_EX+ "                               | |")
    time.sleep(0.75)
    print(Fore.LIGHTWHITE_EX + "                         ~~~~~~~~~~~~~~~~")
    time.sleep(0.75)
    print(Fore.LIGHTWHITE_EX +"                        |                |")
    time.sleep(0.75)
    print(Fore.LIGHTWHITE_EX +"                        | 2022 / 04 / 13 |")
    time.sleep(0.75)
    print(Fore.LIGHTWHITE_EX +"                   _____|                |____")
    time.sleep(0.75)
    print(Fore.MAGENTA +"                  |     `````````````````     |")
    time.sleep(0.75)
    print(Fore.MAGENTA+"                  |       İYİ Kİ DOĞDUN       |")
    time.sleep(0.75)
    print(Fore.MAGENTA+"           _______|                           |______")
    time.sleep(0.75)
    print(Fore.LIGHTMAGENTA_EX +"          |        ```````````````````````````       |")
    time.sleep(0.75)
    print(Fore.LIGHTMAGENTA_EX +"          |               KİSİNİN İSMİ               |")
    time.sleep(0.75)
    print(Fore.LIGHTMAGENTA_EX + "          |            NİCE MUTLU YASLARA            |")
    time.sleep(0.75)
    print(Fore.LIGHTMAGENTA_EX +"          | ________________________________________ |")

Button(root,text="HEDİYEYİ ACMAK İCİN LUTFEN BURAYA BASIN",command=bday).pack()
root.mainloop()
