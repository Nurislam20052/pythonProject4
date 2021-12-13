from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QInputDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 595)
        MainWindow.setStyleSheet("background: #2D882D")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label.setMinimumSize(QtCore.QSize(171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 111, 16))
        self.label_2.setStyleSheet("font-size:13pt;")
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(130, 40, 82, 17))
        self.radioButton.setStyleSheet("")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 40, 121, 17))
        self.radioButton_2.setStyleSheet("front-size:13pt")
        self.radioButton_2.setStyleSheet("front-size:13pt")
        self.radioButton_2.setStyleSheet("front-size:13pt")
        self.radioButton_2.setStyleSheet("front-size:13pt")
        self.radioButton_2.setStyleSheet("front-size:13pt")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(330, 40, 81, 17))
        self.radioButton_3.setStyleSheet("")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(420, 40, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(500, 40, 91, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.label.setStyleSheet("font-size:13pt;\n"
                                 "")
        self.label.setStyleSheet("font-size:13pt;")
        self.label.setStyleSheet("font-size:13pt;")
        self.label.setStyleSheet("font-size:13pt;")
        self.label.setStyleSheet("font-size:13pt;")
        self.label.setStyleSheet("font-size:13pt;")
        self.label.setStyleSheet("font-size:13pt;")
        self.label.setStyleSheet("font-size:13pt;")
        self.radioButton_6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_6.setGeometry(QtCore.QRect(590, 40, 131, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_7.setGeometry(QtCore.QRect(720, 40, 91, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 791, 41))
        self.pushButton.setStyleSheet("font-size:13pt;\n"
                                      "background: #9EED9E;")
        self.pushButton.setStyleSheet("font-size:13pt;\n"
                                      "background: #9EED9E;")
        self.pushButton.setStyleSheet("font-size:13pt;\n"
                                      "background: #9EED9E;")
        self.pushButton.setStyleSheet("font-size:13pt;\n"
                                      "background: #9EED9E;")
        self.pushButton.setStyleSheet("font-size:13pt;\n"
                                      "background: #9EED9E;")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 150, 361, 51))
        self.label_3.setStyleSheet("font-size:17pt;")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 10, 201, 23))
        self.pushButton_2.setStyleSheet("background: #9EED9E;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.product = QtWidgets.QLabel(self.centralwidget)
        self.product.setGeometry(QtCore.QRect(30, 240, 251, 31))
        self.product.setStyleSheet("background:#9EED9E;\n"
                                   "font-size:13pt;")
        self.product.setObjectName("product")
        self.restoraunt = QtWidgets.QLabel(self.centralwidget)
        self.restoraunt.setGeometry(QtCore.QRect(30, 280, 251, 31))
        self.restoraunt.setStyleSheet("background:#9EED9E;\n"
                                      "font-size:13pt;")
        self.restoraunt.setObjectName("restoraunt")
        self.transfer = QtWidgets.QLabel(self.centralwidget)
        self.transfer.setGeometry(QtCore.QRect(30, 320, 251, 31))
        self.transfer.setStyleSheet("background:#9EED9E;\n"
                                    "font-size:13pt;")
        self.transfer.setObjectName("transfer")
        self.car = QtWidgets.QLabel(self.centralwidget)
        self.car.setGeometry(QtCore.QRect(30, 360, 251, 31))
        self.car.setStyleSheet("background:#9EED9E;\n"
                               "font-size:13pt;")
        self.car.setStyleSheet("background:#9EED9E;\n"
                               "font-size:13pt;")
        self.car.setStyleSheet("background:#9EED9E;\n"
                               "font-size:13pt;")
        self.car.setStyleSheet("background:#9EED9E;\n"
                               "font-size:13pt;")
        self.car.setStyleSheet("background:#9EED9E;\n"
                               "font-size:13pt;")
        self.car.setObjectName("car")
        self.home = QtWidgets.QLabel(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(30, 400, 251, 31))
        self.home.setStyleSheet("background:#9EED9E;\n"
                                "font-size:13pt;")
        self.home.setStyleSheet("background:#9EED9E;\n"
                                "font-size:13pt;")
        self.home.setStyleSheet("background:#9EED9E;\n"
                                "font-size:13pt;")
        self.home.setStyleSheet("background:#9EED9E;\n"
                                "font-size:13pt;")
        self.home.setObjectName("home")
        self.arm = QtWidgets.QLabel(self.centralwidget)
        self.arm.setGeometry(QtCore.QRect(30, 440, 251, 31))
        self.arm.setStyleSheet("background:#9EED9E;\n"
                               "font-size:13pt;")
        self.arm.setStyleSheet("background:#9EED9E;\n"
                               "font-size:13pt;")
        self.arm.setStyleSheet("background:#9EED9E;\n"
                               "font-size:13pt;")
        self.arm.setObjectName("arm")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 480, 251, 31))
        self.label_10.setStyleSheet("background:#9EED9E;\n"
                                    "font-size:13pt;")
        self.label_10.setStyleSheet("background:#9EED9E;\n"
                                    "font-size:13pt;")
        self.label_10.setStyleSheet("background:#9EED9E;\n"
                                    "font-size:13pt;")

        self.label_10.setObjectName("label_10")
        self.product_t = QtWidgets.QLabel(self.centralwidget)
        self.product_t.setGeometry(QtCore.QRect(310, 240, 571, 31))
        self.product_t.setStyleSheet("background:#9EED9E;\n"
                                     "font-size:13pt;\n"
                                     "")
        self.product_t.setStyleSheet("background:#9EED9E;\n"
                                     "font-size:13pt;\n"
                                     "")
        self.product_t.setStyleSheet("background:#9EED9E;\n"
                                     "font-size:13pt;\n"
                                     "")
        self.product_t.setText("")
        self.product_t.setObjectName("product_t")
        self.transport_t = QtWidgets.QLabel(self.centralwidget)
        self.transport_t.setGeometry(QtCore.QRect(310, 360, 571, 31))
        self.transport_t.setStyleSheet("background:#9EED9E;\n"
                                       "font-size:13pt;")
        self.transport_t.setStyleSheet("background:#9EED9E;\n"
                                       "font-size:13pt;")
        self.transport_t.setStyleSheet("background:#9EED9E;\n"
                                       "font-size:13pt;")
        self.transport_t.setText("")
        self.transport_t.setObjectName("transport_t")
        self.arm_t = QtWidgets.QLabel(self.centralwidget)
        self.arm_t.setGeometry(QtCore.QRect(310, 440, 571, 31))
        self.arm_t.setStyleSheet("background:#9EED9E;\n"
                                 "font-size:13pt;")
        self.arm_t.setText("")
        self.arm_t.setObjectName("arm_t")
        self.home_t = QtWidgets.QLabel(self.centralwidget)
        self.home_t.setGeometry(QtCore.QRect(310, 400, 571, 31))
        self.home_t.setStyleSheet("background:#9EED9E;\n"
                                  "font-size:13pt;")
        self.home_t.setStyleSheet("background:#9EED9E;\n"
                                  "font-size:13pt;")
        self.home_t.setStyleSheet("background:#9EED9E;\n"
                                  "font-size:13pt;")
        self.home_t.setText("")
        self.home_t.setObjectName("home_t")
        self.chill_t = QtWidgets.QLabel(self.centralwidget)
        self.chill_t.setGeometry(QtCore.QRect(310, 480, 571, 31))
        self.chill_t.setStyleSheet("background:#9EED9E;\n"
                                   "font-size:13pt;")
        self.chill_t.setText("")
        self.chill_t.setObjectName("chill_t")
        self.restoraunt_t = QtWidgets.QLabel(self.centralwidget)
        self.restoraunt_t.setGeometry(QtCore.QRect(310, 280, 571, 31))
        self.restoraunt_t.setStyleSheet("background:#9EED9E;\n"
                                        "font-size:13pt;")
        self.restoraunt_t.setStyleSheet("background:#9EED9E;\n"
                                        "font-size:13pt;")
        self.restoraunt_t.setStyleSheet("background:#9EED9E;\n"
                                        "font-size:13pt;")
        self.restoraunt_t.setText("")
        self.restoraunt_t.setObjectName("restoraunt_t")
        self.transfer_t = QtWidgets.QLabel(self.centralwidget)
        self.transfer_t.setGeometry(QtCore.QRect(310, 320, 571, 31))
        self.transfer_t.setStyleSheet("background:#9EED9E;\n"
                                      "font-size:13pt;")
        self.transfer_t.setText("")
        self.transfer_t.setObjectName("transfer_t")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 530, 131, 23))
        self.pushButton_3.setStyleSheet("background: #9EED9E;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background: #9EED9E;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("background: #9EED9E;")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Учет финансов .by Venz"))
        self.label.setText(_translate("MainWindow", "Сумма траты:"))
        self.label_2.setText(_translate("MainWindow", "Выберите тип траты"))
        self.radioButton.setText(_translate("MainWindow", "Продукты"))
        self.radioButton_2.setText(_translate("MainWindow", "Рестораны и кафе"))
        self.radioButton_3.setText(_translate("MainWindow", "Переводы"))
        self.radioButton_4.setText(_translate("MainWindow", "Транспорт"))
        self.radioButton_5.setText(_translate("MainWindow", "Всё для дома"))
        self.radioButton_6.setText(_translate("MainWindow", "Здоровье и красота"))
        self.radioButton_7.setText(_translate("MainWindow", "Развлечения"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))
        self.label_3.setText(_translate("MainWindow", "Ваша статистика трат:"))
        self.pushButton_2.setText(_translate("MainWindow", "Ввести сумму траты в рублях"))
        self.product.setText(_translate("MainWindow", "Продукты"))
        self.restoraunt.setText(_translate("MainWindow", "Рестораны и кафе"))
        self.transfer.setText(_translate("MainWindow", "Переводы"))
        self.car.setText(_translate("MainWindow", "Транспорт"))
        self.home.setText(_translate("MainWindow", "Всё для дома"))
        self.arm.setText(_translate("MainWindow", "Здоровье и красота"))
        self.label_10.setText(_translate("MainWindow", "Развлечения"))
        self.pushButton_3.setText(_translate("MainWindow", "Сбросить"))
        self.pushButton_2.setText(_translate("MainWindow", "Ввести сумму траты в рублях"))
        self.product.setText(_translate("MainWindow", "Продукты"))
        self.restoraunt.setText(_translate("MainWindow", "Рестораны и кафе"))
        self.transfer.setText(_translate("MainWindow", "Переводы"))
        self.car.setText(_translate("MainWindow", "Транспорт"))
        self.home.setText(_translate("MainWindow", "Всё для дома"))
        self.arm.setText(_translate("MainWindow", "Здоровье и красота"))
        self.label_10.setText(_translate("MainWindow", "Развлечения"))
        self.pushButton_3.setText(_translate("MainWindow", "Сбросить"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.money = 0
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.summa)
        self.radioButton.clicked.connect(self.zz)
        self.radioButton_2.clicked.connect(self.zz)
        self.radioButton_3.clicked.connect(self.zz)
        self.radioButton_4.clicked.connect(self.zz)
        self.radioButton_5.clicked.connect(self.zz)
        self.radioButton_6.clicked.connect(self.zz)
        self.radioButton_7.clicked.connect(self.zz)
        names = []
        cash = []
        db = sqlite3.connect('money_long.sqlite')
        sql = db.cursor()
        na = sql.execute("""SELECT name FROM money""").fetchall()
        ca = sql.execute("""SELECT cash FROM money""").fetchall()
        for i in na:
            names.append(*i)
        for i in ca:
            cash.append(int(*i))
            self.money = sum(cash)
        cashs = {"Развлечения": 0, "Продукты": 0,
                 "Рестораны и кафе": 0, "Переводы": 0,
                 "Транспорт": 0, "Всё для дома": 0,
                 "Здоровье и красота": 0}
        for i in range(len(names)):
            cashs[names[i]] += cash[i]
        precent = {"Развлечения": 0, "Продукты": 0,
                   "Рестораны и кафе": 0, "Переводы": 0,
                   "Транспорт": 0, "Всё для дома": 0,
                   "Здоровье и красота": 0}
        if bool(names):
            for i in cashs:
                precent[i] = ((cashs[i] / self.money * 100) // 1) / 100
            self.product_t.setGeometry(310, 240, int(precent["Продукты"] * 571) + 2, 31)
            self.restoraunt_t.setGeometry(310, 280, int(precent["Рестораны и кафе"] * 571) + 2, 31)
            self.transfer_t.setGeometry(310, 320, int(precent["Переводы"] * 571) + 2, 31)
            self.transport_t.setGeometry(310, 360, int(precent["Транспорт"] * 571) + 2, 31)
            self.home_t.setGeometry(310, 400, int(precent["Всё для дома"] * 571) + 2, 31)
            self.arm_t.setGeometry(310, 440, int(precent["Здоровье и красота"] * 571) + 2, 31)
            self.chill_t.setGeometry(310, 480, int(precent["Развлечения"] * 571) + 2, 31)
            self.product.setText("Продукты - " + str(cashs["Продукты"]) + "₽")
            self.restoraunt.setText("Рестораны и кафе - " + str(cashs["Рестораны и кафе"]) + "₽")
            self.transfer.setText("Переводы - " + str(cashs["Переводы"]) + "₽")
            self.car.setText("Транспорт - " + str(cashs["Транспорт"]) + "₽")
            self.home.setText("Всё для дома - " + str(cashs["Всё для дома"]) + "₽")
            self.arm.setText("Здоровье и красота - " + str(cashs["Здоровье и красота"]) + "₽")
            self.label_10.setText("Развлечения - " + str(cashs["Развлечения"]) + "₽")
        else:
            self.product_t.setGeometry(310, 240, 0 + 2, 31)
            self.restoraunt_t.setGeometry(310, 280, 0 + 2, 31)
            self.transfer_t.setGeometry(310, 320, 0 + 2, 31)
            self.transport_t.setGeometry(310, 360, 0 + 2, 31)
            self.home_t.setGeometry(310, 400, 0 + 2, 31)
            self.arm_t.setGeometry(310, 440, 0 + 2, 31)
            self.chill_t.setGeometry(310, 480, 0 + 2, 31)
            self.home_t.setGeometry(310, 400, 0 + 2, 31)
            self.arm_t.setGeometry(310, 440, 0 + 2, 31)
            self.chill_t.setGeometry(310, 480, 0 + 2, 31)
            self.home_t.setGeometry(310, 400, 0 + 2, 31)
            self.arm_t.setGeometry(310, 440, 0 + 2, 31)
            self.chill_t.setGeometry(310, 480, 0 + 2, 31)
            self.product.setText("Продукты - " + str(cashs["Продукты"]) + "₽")
            self.restoraunt.setText("Рестораны и кафе - " + str(cashs["Рестораны и кафе"]) + "₽")
            self.transfer.setText("Переводы - " + str(cashs["Переводы"]) + "₽")
            self.car.setText("Транспорт - " + str(cashs["Транспорт"]) + "₽")
            self.home.setText("Всё для дома - " + str(cashs["Всё для дома"]) + "₽")
            self.arm.setText("Здоровье и красота - " + str(cashs["Здоровье и красота"]) + "₽")
            self.label_10.setText("Развлечения - " + str(cashs["Развлечения"]) + "₽")
        self.pushButton.clicked.connect(self.adda)
        self.pushButton_3.clicked.connect(self.delete)

    def summa(self):
        name, ok_pressed = QInputDialog.getText(self, "Введите сумму траты",
                                                "Сколько потратил в рублях?")
        if ok_pressed:
            end_name = ""
            last = ""
            self.counting = int(name)
            self.money += int(name)
            for i in range(len(name)):
                end_name += name[i]
                if (i) % 3 == 0:
                    if i != len(name) - 1:
                        end_name += "."
            name = name[::-1]
            r = 0
            for i in range(1, len(name) + 1):
                if (r) % 3 == 0:
                    if i != 1 and i != len(name) + 1:
                        last += "."
                    last += name[i - 1]
                else:
                    last += name[i - 1]
                r += 1
            last = last[::-1]
            self.label.setText("Сумма траты: " + (last) + "₽")

    def zz(self):
        self.radio = self.sender().text()

    def adda(self):
        db = sqlite3.connect('money_long.sqlite')
        sql = db.cursor()
        sql.execute(f"INSERT INTO money(name,cash) VALUES('{self.radio}','{self.counting}')")
        db.commit()
        names = []
        cash = []
        db = sqlite3.connect('money_long.sqlite')
        sql = db.cursor()
        na = sql.execute("""SELECT name FROM money""").fetchall()
        ca = sql.execute("""SELECT cash FROM money""").fetchall()
        db.commit()
        for i in na:
            names.append(*i)
        for i in ca:
            cash.append(int(*i))
        cashs = {"Развлечения": 0, "Продукты": 0,
                 "Рестораны и кафе": 0, "Переводы": 0,
                 "Транспорт": 0, "Всё для дома": 0,
                 "Здоровье и красота": 0}
        for i in range(len(names)):
            cashs[names[i]] += cash[i]
        precent = {"Развлечения": 0, "Продукты": 0,
                   "Рестораны и кафе": 0, "Переводы": 0,
                   "Транспорт": 0, "Всё для дома": 0,
                   "Здоровье и красота": 0}
        for i in cashs:
            precent[i] = ((cashs[i] / self.money * 100) // 1) / 100
        self.product_t.setGeometry(310, 240, int(precent["Продукты"] * 571) + 2, 31)
        self.restoraunt_t.setGeometry(310, 280, int(precent["Рестораны и кафе"] * 571) + 2, 31)
        self.transfer_t.setGeometry(310, 320, int(precent["Переводы"] * 571) + 2, 31)
        self.transport_t.setGeometry(310, 360, int(precent["Транспорт"] * 571) + 2, 31)
        self.home_t.setGeometry(310, 400, int(precent["Всё для дома"] * 571) + 2, 31)
        self.restoraunt_t.setGeometry(310, 280, int(precent["Рестораны и кафе"] * 571) + 2, 31)
        self.transfer_t.setGeometry(310, 320, int(precent["Переводы"] * 571) + 2, 31)
        self.transport_t.setGeometry(310, 360, int(precent["Транспорт"] * 571) + 2, 31)
        self.home_t.setGeometry(310, 400, int(precent["Всё для дома"] * 571) + 2, 31)
        self.arm_t.setGeometry(310, 440, int(precent["Здоровье и красота"] * 571) + 2, 31)
        self.chill_t.setGeometry(310, 480, int(precent["Развлечения"] * 571) + 2, 31)
        self.product.setText("Продукты - " + str(cashs["Продукты"]) + "₽")
        self.restoraunt.setText("Рестораны и кафе - " + str(cashs["Рестораны и кафе"]) + "₽")
        self.transfer.setText("Переводы - " + str(cashs["Переводы"]) + "₽")
        self.car.setText("Транспорт - " + str(cashs["Транспорт"]) + "₽")
        self.home.setText("Всё для дома - " + str(cashs["Всё для дома"]) + "₽")
        self.arm.setText("Здоровье и красота - " + str(cashs["Здоровье и красота"]) + "₽")
        self.label_10.setText("Развлечения - " + str(cashs["Развлечения"]) + "₽")

    def table(self):
        names = []
        cash = []
        db = sqlite3.connect('money_long.sqlite')
        sql = db.cursor()
        na = sql.execute("""SELECT name FROM money""").fetchall()
        ca = sql.execute("""SELECT cash FROM money""").fetchall()
        db.commit()
        for i in na:
            names.append(*i)
        for i in ca:
            cash.append(int(*i))
        cashs = {"Развлечения": 0, "Продукты": 0,
                 "Рестораны и кафе": 0, "Переводы": 0,
                 "Транспорт": 0, "Всё для дома": 0,
                 "Здоровье и красота": 0}
        for i in range(len(names)):
            cashs[names[i]] += cash[i]
        precent = {"Развлечения": 0, "Продукты": 0,
                   "Рестораны и кафе": 0, "Переводы": 0,
                   "Транспорт": 0, "Всё для дома": 0,
                   "Здоровье и красота": 0}
        for i in cashs:
            precent[i] = ((cashs[i] / self.money * 100) // 1) / 100
        self.product_t.setGeometry(310, 240, int(precent["Продукты"] * 571) + 2, 31)
        self.restoraunt_t.setGeometry(310, 280, int(precent["Рестораны и кафе"] * 571) + 2, 31)
        self.transfer_t.setGeometry(310, 320, int(precent["Переводы"] * 571) + 2, 31)
        self.transport_t.setGeometry(310, 360, int(precent["Транспорт"] * 571) + 2, 31)
        self.home_t.setGeometry(310, 400, int(precent["Всё для дома"] * 571) + 2, 31)
        self.arm_t.setGeometry(310, 440, int(precent["Здоровье и красота"] * 571) + 2, 31)
        self.chill_t.setGeometry(310, 480, int(precent["Развлечения"] * 571) + 2, 31)
        self.product.setText("Продукты - " + str(cashs["Продукты"]) + "₽")
        self.restoraunt.setText("Рестораны и кафе - " + str(cashs["Рестораны и кафе"]) + "₽")
        self.transfer.setText("Переводы - " + str(cashs["Переводы"]) + "₽")
        self.car.setText("Транспорт - " + str(cashs["Транспорт"]) + "₽")
        self.home.setText("Всё для дома - " + str(cashs["Всё для дома"]) + "₽")
        self.arm.setText("Здоровье и красота - " + str(cashs["Здоровье и красота"]) + "₽")
        self.label_10.setText("Развлечения - " + str(cashs["Развлечения"]) + "₽")

    def delete(self):
        names, ok_pressed = QInputDialog.getText(self, "Уверен?",
                                                 "Если уверен - впиши \"УВЕРЕН\"")
        if ok_pressed:
            if names == "УВЕРЕН":
                db = sqlite3.connect('money_long.sqlite')
                sql = db.cursor()
                sql.execute("""DELETE FROM money""")
                db.commit()
                names = []
                cash = []
                names = []
                cash = []
                db = sqlite3.connect('money_long.sqlite')
                sql = db.cursor()
                na = sql.execute("""SELECT name FROM money""").fetchall()
                ca = sql.execute("""SELECT cash FROM money""").fetchall()
                db.commit()
                for i in na:
                    names.append(*i)
                for i in ca:
                    cash.append(int(*i))
                cashs = {"Развлечения": 0, "Продукты": 0,
                         "Рестораны и кафе": 0, "Переводы": 0,
                         "Транспорт": 0, "Всё для дома": 0,
                         "Здоровье и красота": 0}
                for i in range(len(names)):
                    cashs[names[i]] += cash[i]
                precent = {"Развлечения": 0, "Продукты": 0,
                           "Рестораны и кафе": 0, "Переводы": 0,
                           "Транспорт": 0, "Всё для дома": 0,
                           "Здоровье и красота": 0}
                for i in cashs:
                    precent[i] = ((cashs[i] / self.money * 100) // 1) / 100
                self.product_t.setGeometry(310, 240, int(precent["Продукты"] * 571) + 2, 31)
                self.restoraunt_t.setGeometry(310, 280, int(precent["Рестораны и кафе"] * 571) + 2, 31)
                self.transfer_t.setGeometry(310, 320, int(precent["Переводы"] * 571) + 2, 31)
                self.transport_t.setGeometry(310, 360, int(precent["Транспорт"] * 571) + 2, 31)
                self.home_t.setGeometry(310, 400, int(precent["Всё для дома"] * 571) + 2, 31)
                self.arm_t.setGeometry(310, 440, int(precent["Здоровье и красота"] * 571) + 2, 31)
                self.chill_t.setGeometry(310, 480, int(precent["Развлечения"] * 571) + 2, 31)
                self.product.setText("Продукты - " + str(cashs["Продукты"]) + "₽")
                self.restoraunt.setText("Рестораны и кафе - " + str(cashs["Рестораны и кафе"]) + "₽")
                self.transfer.setText("Переводы - " + str(cashs["Переводы"]) + "₽")
                self.car.setText("Транспорт - " + str(cashs["Транспорт"]) + "₽")
                self.home.setText("Всё для дома - " + str(cashs["Всё для дома"]) + "₽")
                self.arm.setText("Здоровье и красота - " + str(cashs["Здоровье и красота"]) + "₽")
                self.label_10.setText("Развлечения - " + str(cashs["Развлечения"]) + "₽")
                self.money = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
