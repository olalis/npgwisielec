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

class OstatniaGra(BaseModel):
    poziom = CharField()
    kategoria = CharField()
    haslo = CharField(null=False)
    wynik = IntegerField()
    wykorzystane_litery = CharField()
    ilosc_prob = IntegerField()
    pola_zgadniete = IntegerField()


class Statystyki(BaseModel):
    wygrane = IntegerField()
    przegrane = IntegerField()
    suma_punktow = IntegerField()


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
    # if os.path.exists(baza_nazwa):
    #     os.remove(baza_nazwa)
    # baza.connect()  # połączenie z bazą
    # baza.create_tables([Poziom, Kategoria, Haslo])  # tworzymy tabele
    # 
    # dane = {
    #     Haslo: 'hasla',
    #     Poziom: 'poziomy',
    #     Kategoria: 'kategorie',
    # }
    # 
    # dodaj_dane(dane)
    # baza.commit()

    # WERSJA KOŃCOWA
    sciezka_baza = os.path.abspath("./" + baza_nazwa)

    if not os.path.exists(sciezka_baza):
        Path(sciezka_baza).touch()

        baza.connect(reuse_if_open=True)
        baza.create_tables([Poziom, Kategoria, Haslo, OstatniaGra, Statystyki])

        dane = {
            Haslo: 'hasla',
            Poziom: 'poziomy',
            Kategoria: 'kategorie',
            OstatniaGra: "ostatnia_gra",
            Statystyki: "statystyki"
        }

        dodaj_dane(dane)
        baza.commit()

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


def odczytaj_gre(that):  # funkcja odczytująca stan ostaniej zapsanej gry
    poziom = OstatniaGra.select(OstatniaGra.poziom).scalar()
    kategoria = OstatniaGra.select(OstatniaGra.kategoria).scalar()
    haslo = OstatniaGra.select(OstatniaGra.haslo).scalar()
    wynik = OstatniaGra.select(OstatniaGra.wynik).scalar()
    wykorzystane_litery = OstatniaGra.select(OstatniaGra.wykorzystane_litery).scalar()
    ilosc_prob = OstatniaGra.select(OstatniaGra.ilosc_prob).scalar()
    pola_zgadniete = OstatniaGra.select(OstatniaGra.pola_zgadniete).scalar()
    return poziom, kategoria, haslo, wynik, wykorzystane_litery, ilosc_prob, pola_zgadniete


def zapisz_gre(poziom, kategoria, haslo, wynik, wykorzystane_litery, ilosc_prob, pola_zgadniete, that):
    # funkcja zapisująca stan gry
    stare_dane = OstatniaGra.select().get()
    stare_dane.delete_instance()
    del stare_dane
    that.nowe_dane = OstatniaGra(poziom=poziom, kategoria=kategoria, haslo=haslo, wynik=wynik,
                                  wykorzystane_litery=wykorzystane_litery, ilosc_prob=ilosc_prob,
                                  pola_zgadniete=pola_zgadniete)
    that.nowe_dane.save()


def odczytaj_statystki(that):  # funkcja odczytująca statystyki
    wygrane = Statystyki.select(Statystyki.wygrane).scalar()
    przegrane = Statystyki.select(Statystyki.przegrane).scalar()
    suma_punktow = Statystyki.select(Statystyki.suma_punktow).scalar()
    return wygrane, przegrane, suma_punktow


def zapisz_statystyki(rezultat, punkty, that):  # funkcja zapisująca statystyki
    that.wygrane, that.przegrane, that.suma_punktow = odczytaj_statystki(that)
    if rezultat:
        that.wygrane += 1
    else:
        that.przegrane += 1
    suma = that.suma_punktow + punkty
    stare_dane = Statystyki.select().get()
    stare_dane.delete_instance()
    del stare_dane
    that.nowe_dane = Statystyki(wygrane=that.wygrane, przegrane=that.przegrane, suma_punktow=suma)
    that.nowe_dane.save()