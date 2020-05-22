# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statystyki.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from baza import *
import matplotlib.pyplot as plt


class Ui_statystyki(object):
    def setupUi(self, statystyki):
        statystyki.setObjectName("statystyki")
        statystyki.resize(992, 1109)
        self.centralwidget = QtWidgets.QWidget(statystyki)
        self.centralwidget.setObjectName("centralwidget")
        self.tytul = QtWidgets.QLabel(self.centralwidget)
        self.tytul.setGeometry(QtCore.QRect(425, 10, 441, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tytul.setFont(font)
        self.tytul.setObjectName("tytul")
        self.Ilosc_wyg_tablica = QtWidgets.QLabel(self.centralwidget)
        self.Ilosc_wyg_tablica.setGeometry(QtCore.QRect(20, 100, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Ilosc_wyg_tablica.setFont(font)
        self.Ilosc_wyg_tablica.setObjectName("Ilosc_wyg_tablica")
        self.ilosc_przeg_tablica = QtWidgets.QLabel(self.centralwidget)
        self.ilosc_przeg_tablica.setGeometry(QtCore.QRect(20, 240, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ilosc_przeg_tablica.setFont(font)
        self.ilosc_przeg_tablica.setObjectName("ilosc_przeg_tablica")
        self.wykres_btn = QtWidgets.QPushButton(self.centralwidget)
        self.wykres_btn.setGeometry(QtCore.QRect(425, 500, 111, 31))
        self.wykres_btn.setObjectName("wykres_btn")
        self.wygrane_LCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.wygrane_LCD.setGeometry(QtCore.QRect(40, 140, 141, 81))
        self.wygrane_LCD.setObjectName("wygrane_LCD")
        self.suma_tablica = QtWidgets.QLabel(self.centralwidget)
        self.suma_tablica.setGeometry(QtCore.QRect(620, 100, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.suma_tablica.setFont(font)
        self.suma_tablica.setObjectName("suma_tablica")
        self.suma = QtWidgets.QLCDNumber(self.centralwidget)
        self.suma.setGeometry(QtCore.QRect(600, 140, 350, 81))
        self.suma.setObjectName("suma")
        self.przegrane_LCD = QtWidgets.QLCDNumber(self.centralwidget)
        self.przegrane_LCD.setGeometry(QtCore.QRect(40, 280, 141, 81))
        self.przegrane_LCD.setObjectName("przegrane_LCD")
        statystyki.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(statystyki)
        self.statusbar.setObjectName("statusbar")
        statystyki.setStatusBar(self.statusbar)
        self.retranslateUi(statystyki)
        self.wczytywanie_statystyk()
        self.wykres_btn.clicked.connect(self.tworzenie_wykresu)
        QtCore.QMetaObject.connectSlotsByName(statystyki)


    def wczytywanie_statystyk(self):
        self.liczba_wyg, self.liczba_przeg, self.wynik_punkty=odczytaj_statystki(self)
        self.wygrane_LCD.display(self.liczba_wyg)
        self.suma.display(self.wynik_punkty)
        self.przegrane_LCD.display(self.liczba_przeg)

    def retranslateUi(self, statystyki):
        _translate = QtCore.QCoreApplication.translate
        statystyki.setWindowTitle(_translate("statystyki", "Statystyki gracza"))
        self.tytul.setText(_translate("statystyki", "Statystyki gry:"))
        self.wykres_btn.setText(_translate("statystyki", "wykres"))
        self.Ilosc_wyg_tablica.setText(_translate("statystyki", "Ilość odgadniętych haseł:"))
        self.ilosc_przeg_tablica.setText(_translate("statystyki", "Ilość nieodgadniętych haseł:"))
        self.suma_tablica.setText(_translate("statystyki", "Suma zdobytych punktów :"))


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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statystyki = QtWidgets.QMainWindow()
    ui = Ui_statystyki()
    ui.setupUi(statystyki)
    statystyki.show()
    sys.exit(app.exec_())

