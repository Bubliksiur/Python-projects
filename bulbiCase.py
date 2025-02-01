import tkinter as tk
import random

root = tk.Tk()
root.title("Sklep z broniami")

saldo_gracza = 0

moje_bronie = []

lista_broni = [
    {"nazwa": "Karambit", "cena": 1000},
    {"nazwa": "Nóż motylkowy", "cena": 1200},
    {"nazwa": "AK47", "cena": 350},
    {"nazwa": "M4A4", "cena": 200},
    {"nazwa": "USPS", "cena": 80}
]

def otworz_skrzynie():
    global wylosowana_bron
    wylosowana_bron = random.choice(lista_broni)
    tekst_wynik.config(text=f"Wylosowana broń: {wylosowana_bron['nazwa']}, Cena: {wylosowana_bron['cena']}")
    przycisk_sprzedaj.pack()
    przycisk_zatrzymaj.pack()

def sprzedaj_bron():
    global saldo_gracza
    saldo_gracza += wylosowana_bron["cena"]
    tekst_saldo.config(text=f"Saldo: {saldo_gracza}")
    przycisk_sprzedaj.pack_forget()
    przycisk_zatrzymaj.pack_forget()

def zatrzymaj_bron():
    moje_bronie.append(wylosowana_bron["nazwa"])
    tekst_bronie.config(text=f"Twoje bronie: {', '.join(moje_bronie)}")
    przycisk_sprzedaj.pack_forget()
    przycisk_zatrzymaj.pack_forget()

tekst_wynik = tk.Label(root, text="Kliknij przycisk, aby otworzyć skrzynię")
tekst_wynik.pack()

tekst_saldo = tk.Label(root, text=f"Saldo: {saldo_gracza}")
tekst_saldo.pack()

tekst_bronie = tk.Label(root, text="Twoje bronie: Brak")
tekst_bronie.pack()

przycisk_otworz = tk.Button(root, text="Otwórz skrzynię", command=otworz_skrzynie)
przycisk_otworz.pack()

przycisk_sprzedaj = tk.Button(root, text="Sprzedaj", command=sprzedaj_bron)
przycisk_sprzedaj.pack_forget()

przycisk_zatrzymaj = tk.Button(root, text="Zatrzymaj", command=zatrzymaj_bron)
przycisk_zatrzymaj.pack_forget()

root.mainloop()
