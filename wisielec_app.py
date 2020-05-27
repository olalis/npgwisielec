# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wisielecokno_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from baza import *
from zasadygry import Ui_Zasady_gry
from PyQt5.QtWidgets import QApplication, QWidget
import matplotlib.pyplot as plt


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(922, 650)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../npgwisielec/hangman.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelwisielec = QtWidgets.QLabel(self.centralwidget)
        self.labelwisielec.setGeometry(QtCore.QRect(380, 40, 381, 131))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 74, 135))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(190, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.labelwisielec.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Freestyle Script")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.labelwisielec.setFont(font)
        self.labelwisielec.setStyleSheet("")
        self.labelwisielec.setTextFormat(QtCore.Qt.PlainText)
        self.labelwisielec.setObjectName("labelwisielec")
        self.rozpocznij_bnt = QtWidgets.QPushButton(self.centralwidget)
        self.rozpocznij_bnt.setGeometry(QtCore.QRect(370, 220, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rozpocznij_bnt.setFont(font)
        self.rozpocznij_bnt.setObjectName("rozpocznij_bnt")
        self.podaj_btn = QtWidgets.QLabel(self.centralwidget)
        self.podaj_btn.setGeometry(QtCore.QRect(65, 480, 125, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.podaj_btn.setFont(font)
        self.podaj_btn.setObjectName("podaj_btn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 260, 851, 201))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.hasloedt = QtWidgets.QTextEdit(self.frame)
        self.hasloedt.setGeometry(QtCore.QRect(113, 10, 711, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hasloedt.setFont(font)
        self.hasloedt.setReadOnly(True)
        self.hasloedt.setObjectName("hasloedt")
        self.haslolabel = QtWidgets.QLabel(self.frame)
        self.haslolabel.setGeometry(QtCore.QRect(40, 10, 80, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.haslolabel.setFont(font)
        self.haslolabel.setObjectName("haslolabel")
        self.komunikatlabel = QtWidgets.QLabel(self.frame)
        self.komunikatlabel.setGeometry(QtCore.QRect(30, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.komunikatlabel.setFont(font)
        self.komunikatlabel.setObjectName("komunikatlabel")
        self.komunikatedt = QtWidgets.QTextEdit(self.frame)
        self.komunikatedt.setGeometry(QtCore.QRect(10, 110, 811, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.komunikatedt.setFont(font)
        self.komunikatedt.setReadOnly(True)
        self.komunikatedt.setObjectName("komunikatedt")
        self.koniec_btn = QtWidgets.QPushButton(self.centralwidget)
        self.koniec_btn.setGeometry(QtCore.QRect(720, 530, 111, 31))
        self.koniec_btn.setObjectName("koniec_btn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 160, 821, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_kateg = QtWidgets.QLabel(self.layoutWidget)
        self.label_kateg.setMaximumSize(QtCore.QSize(101, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_kateg.setFont(font)
        self.label_kateg.setObjectName("label_kateg")
        self.horizontalLayout.addWidget(self.label_kateg)
        self.comboBox_kat = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_kat.setMaximumSize(QtCore.QSize(101, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_kat.setFont(font)
        self.comboBox_kat.setObjectName("comboBox_kat")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.comboBox_kat.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_kat)
        self.label_poziom = QtWidgets.QLabel(self.layoutWidget)
        self.label_poziom.setMaximumSize(QtCore.QSize(181, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_poziom.setFont(font)
        self.label_poziom.setObjectName("label_poziom")
        self.horizontalLayout.addWidget(self.label_poziom)
        self.comboBox_pt = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_pt.setMaximumSize(QtCore.QSize(81, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_pt.setFont(font)
        self.comboBox_pt.setObjectName("comboBox_pt")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.comboBox_pt.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_pt)
        self.label_wynik = QtWidgets.QLabel(self.layoutWidget)
        self.label_wynik.setMaximumSize(QtCore.QSize(71, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_wynik.setFont(font)
        self.label_wynik.setObjectName("label_wynik")
        self.horizontalLayout.addWidget(self.label_wynik)
        self.wynik_edt = QtWidgets.QTextEdit(self.layoutWidget)
        self.wynik_edt.setMaximumSize(QtCore.QSize(111, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.wynik_edt.setFont(font)
        self.wynik_edt.setToolTip("")
        self.wynik_edt.setReadOnly(True)
        self.wynik_edt.setObjectName("wynik_edt")
        self.horizontalLayout.addWidget(self.wynik_edt)
        self.podaj_edt = QtWidgets.QLineEdit(self.centralwidget)
        self.podaj_edt.setGeometry(QtCore.QRect(200, 480, 121, 31))
        self.podaj_edt.setObjectName("podaj_edt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 922, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuStatystyki = QtWidgets.QMenu(self.menubar)
        self.menuStatystyki.setObjectName("menuStatystyki")
        self.menuZasady_gry = QtWidgets.QMenu(self.menubar)
        self.menuZasady_gry.setObjectName("menuZasady_gry")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionZapisz_Gr = QtWidgets.QAction(MainWindow)
        self.actionZapisz_Gr.setShortcut("Ctrl+s")
        self.actionZapisz_Gr.setObjectName("actionZapisz_Gr")
        self.actionWczytaj_Gr = QtWidgets.QAction(MainWindow)
        self.actionWczytaj_Gr.setObjectName("actionWczytaj_Gr")
        self.actionWczytaj_Gr.setShortcut("Ctrl+r")
        self.actionWyswietl_zasady_gry = QtWidgets.QAction(MainWindow)
        self.actionWyswietl_zasady_gry.setObjectName("actionWy_wietl_zasady_gry")
        self.actionPokaz_statystyki = QtWidgets.QAction(MainWindow)
        self.actionPokaz_statystyki.setObjectName("actionPoka_statystyki")
        self.menuMenu.addAction(self.actionZapisz_Gr)
        self.menuMenu.addAction(self.actionWczytaj_Gr)
        self.menuStatystyki.addAction(self.actionPokaz_statystyki)
        self.menuZasady_gry.addAction(self.actionWyswietl_zasady_gry)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuStatystyki.menuAction())
        self.menubar.addAction(self.menuZasady_gry.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.koniec_btn.clicked.connect(self.koniec)  # obsługa wcisniecia przycisku koniec
        self.rozpocznij_bnt.clicked.connect(self.rozpoczecie)  # obsluga wcisniecia przycisku rozpocznij gre
        self.ustaw_kat(self.comboBox_kat.currentText())  # ustawienie kategori poczatkowej
        self.comboBox_kat.activated[str].connect(self.ustaw_kat)  # obsluga ustawiania kategorii
        self.ustaw_pt(self.comboBox_pt.currentText())  # ustawienie poziomu tr. poczatkowego
        self.comboBox_pt.activated[str].connect(self.ustaw_pt)  # obsluga ustawianiapoziomu tr.
        self.podaj_edt.returnPressed.connect(self.odczytaj)  # obsluga podawania liter
        self.wynik = None
        self.menuZasady_gry.triggered.connect(self.zasady)  # odczytanie przycisku zasady
        self.menuStatystyki.triggered.connect(self.statystyka) #odczytanie przycisku statystyk
        self.actionZapisz_Gr.triggered.connect(self.zapisz)  # odczytanie przycisku zapisz
        self.actionWczytaj_Gr.triggered.connect(self.wczytaj)  # odczytanie przycisku wczytaj


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wisielec"))
        self.labelwisielec.setText(_translate("MainWindow", "Wisielec"))
        self.rozpocznij_bnt.setText(_translate("MainWindow", "Rozpocznij grę!"))
        self.podaj_btn.setText(_translate("MainWindow", "Podaj literę:"))
        self.haslolabel.setText(_translate("MainWindow", "Hasło:"))
        self.komunikatlabel.setText(_translate("MainWindow", "Komunikat:"))
        self.koniec_btn.setText(_translate("MainWindow", "Koniec"))
        self.label_kateg.setText(_translate("MainWindow", "Kategoria:"))
        self.comboBox_kat.setItemText(0, _translate("MainWindow", "Geografia"))
        self.comboBox_kat.setItemText(1, _translate("MainWindow", "Jedzenie"))
        self.comboBox_kat.setItemText(2, _translate("MainWindow", "Kino"))
        self.comboBox_kat.setItemText(3, _translate("MainWindow", "Sport"))
        self.comboBox_kat.setItemText(4, _translate("MainWindow", "Nauka"))
        self.comboBox_kat.setItemText(5, _translate("MainWindow", "Zwierzęta"))
        self.label_poziom.setText(_translate("MainWindow", "Poziom trudności:"))
        self.comboBox_pt.setItemText(0, _translate("MainWindow", "Łatwy"))
        self.comboBox_pt.setItemText(1, _translate("MainWindow", "Średni"))
        self.comboBox_pt.setItemText(2, _translate("MainWindow", "Trudny"))
        self.label_wynik.setText(_translate("MainWindow", "Wynik:"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.menuStatystyki.setTitle(_translate("MainWindow", "Statystyki"))
        self.menuZasady_gry.setTitle(_translate("MainWindow", "Zasady gry"))
        self.actionZapisz_Gr.setText(_translate("MainWindow", "Zapisz Grę"))
        self.actionWczytaj_Gr.setText(_translate("MainWindow", "Wczytaj Grę"))
        self.actionWyswietl_zasady_gry.setText(_translate("MainWindow", "Wyświetl zasady gry"))
        self.actionPokaz_statystyki.setText(_translate("MainWindow", "Pokaż statystyki"))


    def koniec(self):
        if self.wynik is not None and not self.czy_wygrana() and self.liczba_prob != 0:
            self.zapytanie = QtWidgets.QWidget()
            self.ui3 = Ui_Form()
            self.ui3.setupUi(self.zapytanie)
            self.zapytanie.setFocus()
            self.zapytanie.show()
            self.ui3.Tak.clicked.connect(self.tak)
            self.ui3.Nie.clicked.connect(self.nie)
        else:
            baza.close()
            exit()  # funkcjonalność przycisku koniec


    def tak(self):
        self.zapisz()
        baza.close()
        exit()

    def nie(self):
        baza.close()
        exit()


    def rozpoczecie(self):  # funkcja realizująca rozpoczecie gry
        self.liczba_prob = 10
        self.wynik = 0
        self.wylosowane_haslo = pobierz_haslo(self)
        self.komunikatedt.setText(str(
            "Rozpoczęto grę na poziomie " + self.poziom_tr + "m. Hasło z kategorii " + self.kategoria + " zostało wylosowane.\nPodaj pierwszą literę:\t\t\t\t Pozostało prób:" + str(
                self.liczba_prob)))
        self.hasloedt.setText(str(len(self.wylosowane_haslo) * '*  '))
        self.wynik_edt.setText(str(self.wynik))
        self.wykorzystane_litery = []
        self.indeksy = []
        for i in range(len(self.wylosowane_haslo)):
            self.indeksy.append(False)

    def czy_wygrana(self):  # fukcja sprawdzająca czy wszystkie litery zostały odgadnięte
        self.zgadniete = 0
        for i in range(len(self.wylosowane_haslo)):
            if self.indeksy[i]:
                self.zgadniete += 1
        if self.zgadniete == len(self.wylosowane_haslo):
            self.komunikatedt.setText("Gratulacje wygrałeś!!!\nTwój wynik końcowy: " + str(self.wynik_koncowy()))
            self.wynik_edt.setText(str(self.wynik_koncowy()))
            zapisz_statystyki(1, self.wynik_koncowy(), self)

            return True

    def wynik_koncowy(self):  # funkcja zwracajaca wynik koncowy uzalezniony od poziomu trudnosci
        if self.poziom_tr == "Łatwy":
            return self.wynik
        elif self.poziom_tr == "Średni":
            return 3 * self.wynik
        elif self.poziom_tr == "Trudny":
            return 5 * self.wynik

    def odczytaj(self):  # funkcja odczytująca podawane litery
        self.furtka_omijajaca_warunki_rozpoczecia = 0
        self.podana_litera = self.podaj_edt.text().upper()  # umożliwia poprawne odczytanie malych badz duzych liter
        if (self.wynik is not None and not self.czy_wygrana() and self.liczba_prob != 0) or self.furtka_omijajaca_warunki_rozpoczecia == 1:  # wymuszenie kliknięcia rozpocznij grę na początku i po zakonczeniu gry z jednym hasłem
            if len(self.podana_litera) == 1:  # sprawdzenie czy podana litera sklada się z jednego znaku
                if self.podana_litera in self.wylosowane_haslo and self.podana_litera not in self.wykorzystane_litery:  # funkcjonalność gdy litera zgadnieta
                    self.wykorzystane_litery.append(self.podana_litera)
                    self.komunikatedt.setText("Brawo! Zgadłeś! \t\t\t\t Pozostało prób:" + str(
                        self.liczba_prob) + "\nWykorzystane litery:" + str(
                        self.wykorzystane_litery) + "\nPodaj następną literę: ")
                    for i in range(len(self.wylosowane_haslo)):
                        if self.wylosowane_haslo[i] == self.podana_litera:
                            self.wynik += 500
                            self.indeksy[i] = True
                    self.wynik_edt.setText(str(self.wynik))

                    self.haslo_kom = " ".join(
                        [litera if self.indeksy[i] else "*" for i, litera in enumerate(self.wylosowane_haslo)])
                    self.hasloedt.setText(self.haslo_kom.strip())
                    self.czy_wygrana()

                elif self.podana_litera in self.wykorzystane_litery:  # komunikat gdy podaliśmy już wcześniej tą samą literę
                    self.komunikatedt.setText("Już podałeś tą literę!\t\t\t\t Pozostało prób:" + str(
                        self.liczba_prob) + "\nWykorzystane litery:" + str(
                        self.wykorzystane_litery) + "\nPodaj następną literę: ")
                else:
                    self.wykorzystane_litery.append(self.podana_litera)  # funkcjonalność gdy litery nie ma w haśle
                    self.liczba_prob -= 1
                    self.wynik -= 100
                    self.komunikatedt.setText(
                        "Pudło!\t\t\t\t Pozostało prób:" + str(self.liczba_prob) + "\nWykorzystane litery:" + str(
                            self.wykorzystane_litery) + "\nPodaj następną literę: ")
                    self.wynik_edt.setText(str(self.wynik))
                    if self.liczba_prob == 0:
                        self.komunikatedt.setText("\tGAME OVER!!!")
                        zapisz_statystyki(0, self.wynik, self)
            else:
                self.komunikatedt.setText(
                    "Wprowadzono błędne dane! Spróbuj ponownie")  # komunikat przy wprowadzeniu błednych danych
            self.podaj_edt.setText("")
        else:
            self.komunikatedt.setText(
                "Aby rozpocząć grę wybierz ustawienia i kliknij Rozpocznij grę.")  # komunikat gdy gra nie zaczęta lub zakonczona po podaniu litery
            self.podaj_edt.setText("")

    def ustaw_kat(self, wartosc):  # funkcja wykrywa ustawienie innej kategorii niz poczatkowa(pierwsza w comboboxie)
        self.kategoria = wartosc

    def ustaw_pt(self, wartosc):  # funkcja wykrywa ustawienie innego poziomu tr. niz poczatkowy(pierwsza w comboboxie)
        self.poziom_tr = wartosc

    def zasady(self):  # funkcja otwierająca okno z zasadami gry
        self.zasadyshow = QtWidgets.QWidget()
        self.ui2 = Ui_Zasady_gry()
        self.ui2.setupUi(self.zasadyshow)
        self.zasadyshow.setFocus()
        self.zasadyshow.show()
        
    def statystyka(self):
        self.statyshow = QtWidgets.QMainWindow()
        self.ui4 = Ui_statystyki()
        self.ui4.setupUi(self.statyshow)
        self.statyshow.setFocus()
        self.statyshow.show()
      
# Poniżej znajduje się blok kodu obsługujący funkcjonalność zapis/odczyt
    def wczytaj(self):
        self.czy_sprawdzamy = False  # Jeśli chcesz uzyskać informację o wczytywanych zmiennych ustaw wartość True
        self.furtka_omijajaca_warunki_rozpoczecia = 1
        self.poziom_tr, self.kategoria, self.wylosowane_haslo, self.wynik, self.st, self.liczba_prob, self.zgadniete = odczytaj_gre(
            self)
        if self.czy_sprawdzamy:  # sprawdzanie poprawności typu lub sprawdzanie argumentu
            print(type(self.wykorzystane_litery))
            print(self.wykorzystane_litery)
            print(type(self.poziom_tr))
            print(self.poziom_tr)
            print(type(self.kategoria))
            print(self.kategoria)
            print(type(self.wylosowane_haslo))
            print(self.wylosowane_haslo)
            print(type(self.wynik))
            print(self.wynik)
            print(type(self.st))
            print(self.st)
            print(type(self.liczba_prob))
            print(self.liczba_prob)
            print(type(self.zgadniete))
            print(self.zgadniete)
        self.indeksy = []
        self.wykorzystane_litery = []
        for i in range(len(self.st)):
            self.wykorzystane_litery.append(self.st[i])
        for i in range(len(self.wylosowane_haslo)):
            self.indeksy.append(False)
        for i in range(len(self.wylosowane_haslo)):
            if self.wylosowane_haslo[i] in self.wykorzystane_litery:
                self.indeksy[i] = True
        self.haslo_kom = " ".join(
            [litera if self.indeksy[i] else "*" for i, litera in enumerate(self.wylosowane_haslo)])
        self.hasloedt.setText(self.haslo_kom.strip())
        self.wynik_edt.setText(str(self.wynik))
        self.komunikatedt.setText(str(
            "Wznowiono grę " + self.kategoria + " / " + self.poziom_tr +
            ". \tPozostało prób:" + str(self.liczba_prob)) + "\nWykorzystane litery:" + str(
            self.wykorzystane_litery) + "\nPodaj następną literę: ")

    def zapisz(self):
        self.czy_sprawdzamy = False  # Jeśli chcesz uzyskać informację o wczytywanych zmiennych ustaw wartość True
        if self.czy_sprawdzamy :  # sprawdzanie poprawności typu lub sprawdzanie argumentu
            print(type(self.wykorzystane_litery))
            print(self.wykorzystane_litery)
            print(type(self.poziom_tr))
            print(self.poziom_tr)
            print(type(self.kategoria))
            print(self.kategoria)
            print(type(self.wylosowane_haslo))
            print(self.wylosowane_haslo)
            print(type(self.wynik))
            print(self.wynik)
            print(type(self.st))
            print(self.st)
            print(type(self.liczba_prob))
            print(self.liczba_prob)
            print(type(self.zgadniete))
            print(self.zgadniete)
        if self.wynik is not None and not self.czy_wygrana() and self.liczba_prob != 0:
            self.st = ''.join(self.wykorzystane_litery)
            zapisz_gre(self.poziom_tr, self.kategoria, self.wylosowane_haslo, self.wynik, self.st, self.liczba_prob,
                       self.zgadniete, self)
            self.komunikatedt.setText(str("\t\t\tGra została poprawnie zapisana \n" "Pozostało prób:" + str(self.liczba_prob) + "\nWykorzystane litery:" + str(
                            self.wykorzystane_litery) + "\t\t\t\tPodaj następną literę: "))
        else:
            self.komunikatedt.setText(str("\t\t\t Gra się jeszcze nie rozpoczęła"
                                          "\n\t\t Wybierz kategorię i hasło, a następnie kliknij"
                                          "\n\t\t\t\t Rozpocznij grę!"))
# Koniec bloku kodu obsługującego funkcjonalność zapis/odczyt

# Poniżej znajduje się kod okna pytającego o zapis
class Ui_Form(object):
    def __init__(self):
        self.label = None
        self.Tak = None
        self.Nie = None
    def setupUi(self, Form):
        Form.setObjectName("Zapis?")
        Form.resize(640, 190)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 10, 201, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../npgwisielec/hangman.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.label.setStyleSheet("font: 36pt \"Freestyle Script\";")
        self.label.setObjectName("label")
        self.Tak = QtWidgets.QPushButton(Form)
        self.Tak.setGeometry(QtCore.QRect(180, 110, 111, 51))
        self.Tak.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.Tak.setObjectName("Tak")
        self.Nie = QtWidgets.QPushButton(Form)
        self.Nie.setGeometry(QtCore.QRect(310, 110, 111, 51))
        self.Nie.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";")
        self.Nie.setObjectName("nie")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Zapis?"))
        self.label.setText(_translate("Form", " Zapis gry?"))
        self.Tak.setText(_translate("Form", "TAK"))
        self.Nie.setText(_translate("Form", "NIE"))
# Koniec kodu okna pytającego o zapis

# Poniżej znajduje się kod okna statystyk                                                                             
class Ui_statystyki(QWidget):                                                                               
    def setupUi(self, statystyki):                                                                          
        statystyki.setObjectName("statystyki")                                                              
        statystyki.resize(1020, 475)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../npgwisielec/hangman.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        statystyki.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(statystyki)                                                  
        self.centralwidget.setObjectName("centralwidget")                                                   
        self.tytul = QtWidgets.QLabel(self.centralwidget)                                                   
        self.tytul.setGeometry(QtCore.QRect(300, 10, 441, 71))
        self.tytul.setStyleSheet("color: rgb(0, 0, 127);")
        font = QtGui.QFont()                                                                                
        font.setPointSize(40)                                                                               
        font.setFamily("Freestyle Script")                                                                  
        font.setBold(False)                                                                                 
        font.setItalic(True)                                                                                
        font.setWeight(50)                                                                                  
        self.tytul.setFont(font)                                                                            
        self.tytul.setObjectName("tytul")                                                                   
        self.Ilosc_wyg_tablica = QtWidgets.QLabel(self.centralwidget)                                       
        self.Ilosc_wyg_tablica.setGeometry(QtCore.QRect(20, 100, 450, 90))
        font = QtGui.QFont()                                                                                
        font.setPointSize(20)                                                                               
        self.Ilosc_wyg_tablica.setFont(font)                                                                
        self.Ilosc_wyg_tablica.setObjectName("Ilosc_wyg_tablica")                                           
        self.ilosc_przeg_tablica = QtWidgets.QLabel(self.centralwidget)                                     
        self.ilosc_przeg_tablica.setGeometry(QtCore.QRect(20, 260, 420, 90))
        font = QtGui.QFont()                                                                                
        font.setPointSize(20)                                                                               
        self.ilosc_przeg_tablica.setFont(font)                                                              
        self.ilosc_przeg_tablica.setObjectName("ilosc_przeg_tablica")                                       
        self.wykres_btn = QtWidgets.QPushButton(self.centralwidget)                                         
        self.wykres_btn.setGeometry(QtCore.QRect(550, 330, 120, 40))                                        
        self.wykres_btn.setObjectName("wykres_btn")                                                         
        self.wygrane_LCD = QtWidgets.QLCDNumber(self.centralwidget)                                         
        self.wygrane_LCD.setGeometry(QtCore.QRect(40, 180, 150, 80))
        self.wygrane_LCD.setObjectName("wygrane_LCD")                                                       
        self.suma_tablica = QtWidgets.QLabel(self.centralwidget)                                            
        self.suma_tablica.setGeometry(QtCore.QRect(520, 100, 400, 90))
        font = QtGui.QFont()                                                                                
        font.setPointSize(20)                                                                               
        self.suma_tablica.setFont(font)                                                                     
        self.suma_tablica.setObjectName("suma_tablica")                                                     
        self.suma = QtWidgets.QLCDNumber(self.centralwidget)                                                
        self.suma.setGeometry(QtCore.QRect(550, 180, 350, 80))
        self.suma.setObjectName("suma")                                                                     
        self.przegrane_LCD = QtWidgets.QLCDNumber(self.centralwidget)                                       
        self.przegrane_LCD.setGeometry(QtCore.QRect(40, 340, 150, 80))
        self.przegrane_LCD.setObjectName("przegrane_LCD")                                                   
        statystyki.setCentralWidget(self.centralwidget)                                                     
        self.statusbar = QtWidgets.QStatusBar(statystyki)                                                   
        self.statusbar.setObjectName("statusbar")                                                           
        statystyki.setStatusBar(self.statusbar)                                                             
        self.retranslateUi(statystyki)                                                                      
        self.wczytywanie_statystyk()                                                                        
        self.wykres_btn.clicked.connect(self.tworzenie_wykresu)                                             
        QtCore.QMetaObject.connectSlotsByName(statystyki)                                                   
                                                                                                            
                                                                                                            
    def retranslateUi(self, statystyki):                                                                    
        _translate = QtCore.QCoreApplication.translate                                                      
        statystyki.setWindowTitle(_translate("statystyki", "Statystyki gracza"))                            
        self.tytul.setText(_translate("statystyki", "Statystyki gry:"))                                     
        self.wykres_btn.setText(_translate("statystyki", "Wykres"))
        self.Ilosc_wyg_tablica.setText(_translate("statystyki", "Ilość odgadniętych haseł:"))               
        self.ilosc_przeg_tablica.setText(_translate("statystyki", "Ilość nieodgadniętych haseł:"))          
        self.suma_tablica.setText(_translate("statystyki", "Suma zdobytych punktów:"))                      
                                                                                                            
    def wczytywanie_statystyk(self):
        self.liczba_wyg, self.liczba_przeg, self.wynik_punkty= odczytaj_statystki(self)                     
        self.wygrane_LCD.display(self.liczba_wyg)                                                           
        self.suma.display(self.wynik_punkty)                                                                
        self.przegrane_LCD.display(self.liczba_przeg)                                                       
                                                                                                            
    def tworzenie_wykresu(self):                                                                            
        self.liczba_wyg, self.liczba_przeg, self.wynik_punkty=odczytaj_statystki(self)                      
        plt.style.use("fivethirtyeight")                                                                    
        labels = 'wygrane', 'przegrane'                                                                     
        sizes=[self.liczba_wyg, self.liczba_przeg]                                                          
        colors=['green','red']                                                                              
        plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=150)                         
        print("")                                                                                           
        plt.axis('scaled')                                                                                  
        plt.tight_layout()                                                                                  
        plt.show()                                                                                          
                                                                                                            
#koniec kodu statystyk                                                                                      
                                                                                                            
if __name__ == "__main__":                                                                                  
    import sys                                                                                              
    polacz()                                                                                                
    app = QApplication(sys.argv)                                                                            
    MainWindow = QtWidgets.QMainWindow()                                                                    
    ui = Ui_MainWindow()                                                                                    
    ui.setupUi(MainWindow)                                                                                  
    MainWindow.show()                                                                                       
    sys.exit(app.exec_())                                                                                                                                                                                                                                                  
