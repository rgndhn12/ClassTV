#Dahan, Regine Fae M. Dahan BSCPE 1-5 ( Introduction to OOP )

#introduction
import pyfiglet
import time
import colorama
from colorama import Fore
colorama.init()
border = "✪" * 75
border_2 = " ☪ " * 25
print(border_2)
print(border)
print(Fore.LIGHTMAGENTA_EX+pyfiglet.figlet_format("TELEVISION",font="advenger"))
print(Fore.LIGHTWHITE_EX+border)
print(border_2)
time.sleep(5)

from ClassTV import Tv

tv_one = Tv(30, 3, True)
tv_two = Tv(3, 2, False)

#print the output
print(Fore.LIGHTMAGENTA_EX+pyfiglet.figlet_format(" THE CHANNEL AND VOLUME LEVEL IS...",font="contessa"))
print(Fore.LIGHTWHITE_EX+border_2)
time.sleep(5)
print(Fore.LIGHTYELLOW_EX+pyfiglet.figlet_format(f"tv1's channel is {tv_one.get_channel()} , volume level is {tv_one.get_volume()}", font="digital"))
print(Fore.LIGHTWHITE_EX+border_2)
time.sleep(5)
print(Fore.CYAN+pyfiglet.figlet_format(f"tv2's channel is {tv_two.get_channel()} , volume level is {tv_two.get_volume()}", font="digital"))
print(Fore.LIGHTWHITE_EX+border_2)




