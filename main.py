import rich
from rich import print
import colorama
from colorama import Fore, Back, Style
import requests
import re, os
import urllib.request
import time
from time import sleep
import bs4
from bs4 import BeautifulSoup
import tqdm
from tqdm import tqdm

print("""[bold yellow]
\n
___________.__            .______.          __________.__          __          
\_   _____/|__| ____    __| _/\_ |__ ___.__.\______   \  | _____ _/  |_  ____  
 |    __)  |  |/    \  / __ |  | __ <   |  | |     ___/  | \__  \\   __\/ __ \ 
 |     \   |  |   |  \/ /_/ |  | \_\ \___  | |    |   |  |__/ __ \|  | \  ___/ 
 \___  /   |__|___|  /\____ |  |___  / ____| |____|   |____(____  /__|  \___  >
     \/            \/      \/      \/\/                         \/          \/ 
""")
print("[bold blue]to select a option type[/bold blue] [bold yellow]PLATE[/bold yellow] [bold blue]or[/bold blue] [bold yellow]VIN[/bold yellow]")
print("""[bold blue]
[+] PLATE number
[+] VIN number
[/bold blue]""")
ans = input(Style.BRIGHT + Fore.RED + "[+] PLATE/VIN: ")

headers = {
'User-Agent': 'Mozilla/5.0 (Linux; Android 13; SM-T220) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

sleep(2)
if ans=="VIN":
   print("[bold blue]type the [/bold blue][bold yellow]vin number[/bold yellow]")
   vin = input(Style.BRIGHT + Fore.RED + "[+] vin number: ")
   print("[bold blue]+-------------------------------------------------------+[/bold blue]")
   print("[dim cyan] INFO: [/dim cyan][bold red]"+vin+"[/bold red]")
   print("[bold blue]+-------------------------------------------------------+[/bold blue]")
   sleep(0.1)
   url = 'https://www.vinfreecheck.com/vin/'+vin+'/vehicle-specification'

   r = requests.get(url, headers=headers)
   html = BeautifulSoup(r.text, "html.parser")
   print("[bold yellow]status code of url[/bold yellow]",r.status_code)
   sleep(2)
   print("[bold blue]using the VIN lookup tool [/bold blue][bold yellow]vinfreecheck[/bold yellow] [bold blue]to lookup[/bold blue][bold red]"+vin+"[/bold red]")
   sleep(0.2)
   for _ in tqdm(range(100),

         desc = "loading report...",
         ascii = False,ncols=100):
         time.sleep(0.1)
   print("[bold green]--!-- Done --!--[/bold green]")
   sleep(4)
   tag1 = html.find(["p"], class_="h2 subtitle-2")
   print("[bold blue]+---------------------------------+[/bold blue]")
   print("[dim cyan]INFO: [/dim cyan][bold red][+] "+tag1.string+"[/bold red]")

   tag2 = html.find_all(["td", "div"], class_="txt")
   for tag2 in tag2:
      print("[bold blue]+--------------------------------------------+[/bold blue]")
      print("[dim cyan]VIN LOOKUP INFO: [/dim cyan][bold red][+] "+tag2.string+"[/bold red]")
      sleep(1)

elif ans=="PLATE":
     print("[bold blue]type the [/bold blue][bold yellow]plate [/bold yellow][bold blue]for ex.([/bold blue][bold yellow]AZO786[/bold yellow][bold blue])[/bold blue]")
     time.sleep(1)
     plate = input(Style.BRIGHT + Fore.RED + "[+] plate: ")
     print("[bold blue]now type the [/bold blue][bold yellow]State[/bold yellow][bold blue] for the given plate [/bold blue][bold red]"+plate+"[/bold red]")
     sleep(1)
     print("[bold blue]listing all [/bold blue][bold yellow]states[/bold yellow]")
     sleep(2)
     print("""[bold yellow]
AL - alabama
AK - alaska
AZ - arizona
AR - arkansas
CA - california
CO - colorado
CT - connecticut
DE - delaware
DC - district of columbia
FL - florida
GA - Georgia
HI - hawaii
ID - idaho
IL - illinois
IN - indiana
IA - iowa
KS - kansas
KY - kentucky
LA - louisiana
ME - maine
MD - maryland
MA - massachusetts
MI - michigan
MN - minnesota
MS - mississippi
MO - missouri
MT - montana
NE - nebraska
NV - nevada
MH - new hampshire
NJ - new jersey
NM - new mexico
NY - new york
NC - north carolina
ND - north dakota
OH - ohio
OK - oklahoma
OR - oregon
PA - pennsylvania
PR - puerto rico
RI - rhode island
SC - south carolina
SD - south dakota
TN - tennessee
TX - texas
UT - utah
VT - vermont
VA - virginia
WA - washington
WV - west virginia
WI - wisconsin
WY - wyoming
     [/bold yellow]""")
     state = input(Style.BRIGHT + Fore.RED + "[+] state: ")
     print("[bold blue]+-------------------------------------------------------+[/bold blue]")
     print("[dim cyan]INFO: [/dim cyan][bold red]"+plate+" "+state+"[/bold red]")
     print("[bold blue]+-------------------------------------------------------+[/bold blue]")
     sleep(0.1)
     url2 = 'https://findbyplate.com/US/'+state+'/'+plate+'/'

     rs = requests.get(url2, headers=headers)
     plate = BeautifulSoup(rs.text, "html.parser")
     print("[bold yellow]status code of url[/bold yellow]", rs.status_code)
     sleep(1)
     print("[bold blue]using the plate lookup tool [/bold blue][bold yellow]FindbyPlate[/bold yellow] [bold blue]to lookup[/bold blue][bold red]"+plate+"[/bold red]")
     sleep(0.2)
     for _ in tqdm(range(100),

         desc = "loading report...",
         ascii = False,ncols=100):
         time.sleep(0.1)
     print("[bold green]--!-- Done --!--[/bold green]")
     time.sleep(4)
     tag_plate = plate.find_all(["div", "/div"], class_="cell" or "clearfix")
     try:
        for tag_plate in tag_plate:
           print("[bold blue]+--------------------------------------------------------+[/bold blue]")
           print("[dim cyan]PLATE LOOKUP INFO: [/dim cyan][bold red][+] "+tag_plate.string)
           sleep(1)
     except TypeError:
           print("done")

else:
    print("[bold yellow]no option named "+ans+"[/bold yellow]")
