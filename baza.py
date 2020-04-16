# -*- coding: utf-8 -*-

from peewee import *
import os.path
from pathlib import Path
import csv

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


def czytaj_dane(): #funkcja odczytująca dane z plików csv
    pass


def dodaj_dane(dane): #funkcja dodająca dane odczytane z plików csv
    pass


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
