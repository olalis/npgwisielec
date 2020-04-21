# -*- coding: utf-8 -*-

from peewee import *
import os.path
from pathlib import Path
import csv
from wisielec_app import *

baza_nazwa = 'wisielec.db'
baza = SqliteDatabase(baza_nazwa)  # instancja bazy


#######MODEL##########
class BaseModel(Model):
    class Meta:
        database = baza


class Poziom(BaseModel):
    poziom = CharField(null=False)


class Kategoria(BaseModel):
    kategoria = CharField(null=False)


class Haslo(BaseModel):
    poziom = ForeignKeyField(Poziom, related_name='poziom')
    kategoria = ForeignKeyField(Kategoria, related_name='kategoria')
    haslo = CharField()

    class Meta:
        order_by = ('haslo',)


########KONIEC##########


def czy_jest(plik):  # funkcja sprawdza, czy plik istnieje na dysku
    if not os.path.isfile(plik):
        print("Plik {} nie istnieje!".format(plik))
        return False
    return True


def czytaj_dane(plik, separator=";"):  # funkcja odczytująca dane z plików csv
    dane = []  # pusta lista na rekordy

    if not czy_jest(plik):
        return dane

    with open(plik, 'r', newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=separator)
        for rekord in tresc:
            dane.append(rekord)
    return dane


def dodaj_dane(dane):  # funkcja dodająca dane odczytane z plików csv
    for model, plik in dane.items():
        pola = [pole for pole in model._meta.fields]
        pola.pop(0)  # usuwamy pola id
        wpisy = czytaj_dane(plik + '.csv', ';')
        model.insert_many(wpisy).execute()


def polacz():
    # WERSJA TESTOWA
    if os.path.exists(baza_nazwa):
        os.remove(baza_nazwa)
    baza.connect()  # połączenie z bazą
    baza.create_tables([Poziom, Kategoria, Haslo])  # tworzymy tabele

    dane = {
        Haslo: 'hasla',
        Poziom: 'poziomy',
        Kategoria: 'kategorie',
    }

    dodaj_dane(dane)
    baza.commit()

    # WERSJA KOŃCOWA
    # sciezka_baza = os.path.abspath("./" + baza_nazwa)
    # 
    # if not os.path.exists(sciezka_baza):
    #     Path(sciezka_baza).touch()
    # 
    #     baza.connect(reuse_if_open=True)
    #     baza.create_tables([Poziom, Kategoria, Haslo])
    # 
    #     dane = {
    #         Haslo: 'hasla',
    #         Poziom: 'poziomy',
    #         Kategoria: 'kategorie',
    #     }
    # 
    #     dodaj_dane(dane)
    #     baza.commit()

    return True


def wykryj_poziom(that):  # funkcja zmieniająca nazwe poziomu (pobraną z comboboxa) na jego indeks
    if that.poziom_tr == "Łatwy":
        poz = 1
    elif that.poziom_tr == "Średni":
        poz = 2
    else:
        poz = 3
    return poz


def wykryj_kategorie(that):  # funkcja zmieniająca nazwe kategori (pobraną z comboboxa) na jej indeks
    if that.kategoria == "Geografia":
        kat = 1
    elif that.kategoria == "Jedzenie":
        kat = 2
    elif that.kategoria == "Kino":
        kat = 3
    elif that.kategoria == "Sport":
        kat = 4
    elif that.kategoria == "Nauka":
        kat = 5
    else:
        kat = 6
    return kat


def pobierz_haslo(that):  # funkcja wybierająca hasło o podanym poziomie i kategori z bazy danych
    haslo = Haslo.select(Haslo.haslo).where(Haslo.kategoria == wykryj_kategorie(that),
                                            Haslo.poziom == wykryj_poziom(that)).order_by(fn.Random()).scalar()
    return haslo
