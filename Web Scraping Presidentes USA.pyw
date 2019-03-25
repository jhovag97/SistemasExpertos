from bs4 import BeautifulSoup
import urllib3
import pandas as pd
from tabulate import tabulate
from tkinter import *

http = urllib3.PoolManager()
urllib3.disable_warnings()
url = 'https://es.wikipedia.org/wiki/Anexo:Presidentes_de_los_Estados_Unidos_por_edad'

responde = http.request('GET',url)
soup = BeautifulSoup(responde.data,"html.parser")

arrayPresidentes = []

table = soup.find('table').find_all('tr')[1::1]

for items in table:
    
    dato = items.find_all(['th','td'])
    
    nombre = dato[1].a.text
    edad = dato[4].get_text('title')
    edad = edad.replace(" años y","").replace(" años y","").replace(" días","")
    
    edadAnios = int(edad[0:2])
    edadDias = int(edad[3:len(edad)])/365
    edad = edadAnios+edadDias
    
    presidente = [nombre, edad]
    arrayPresidentes.append(presidente)

df = arrayPresidentes

tablaPresidentes=tabulate( df, headers=["Nombre", "Edad Actual"], tablefmt='psql')

root = Tk()
root.title("Web Scraping en Python")
texto = StringVar()
texto.set(tablaPresidentes)

Label(root, text="Web Scraping Presidentes USA por edad").pack(anchor="center")
Label(root, text="Sistemas Expertos").pack(anchor="center")
Label(root, text="By Jhovani García Jaime").pack(anchor="center")

label = Label()
label.config(bg="skyblue", fg="black", font=("Consolas",12),textvariable=texto)
label.pack(anchor="center")

root.mainloop()
