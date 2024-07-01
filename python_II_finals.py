import sqlite3
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
import pymongo
from pymongo import MongoClient

# 1
shopping_cart = [["pear", 1], ["orange", 1], ["apple", 2], ["tomatoes", 2], ["yoghurt", 3]]
reversed_cart = []
for i in range(len(shopping_cart) - 1, -1, -1):
    reversed_cart.append(shopping_cart[i])
# print(reversed_cart)
conn = sqlite3.connect('shopping_cart.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Cart (
    id INTEGER PRIMARY KEY,
    product_name TEXT,
    quantity INTEGER
)
''')

cursor.execute('DELETE FROM Cart')

for item in reversed_cart:
    cursor.execute('INSERT INTO Cart (product_name, quantity) VALUES (?, ?)', (item[0], item[1]))

conn.commit()

cursor.execute('SELECT * FROM cart')
rows = cursor.fetchall()

print("Data from the database:")
for row in rows:
    print(row)

conn.close()

# 2
menu = {"cola": 1.99, "fries": 2.99, "burger": 3.99, "shake": 3.5, "soda": 2.4, "chicken strips": 3.9}


def get_order(its):
    print("Menu items:")
    for it in menu.keys():
        print(it)
    order = []
    while True:
        item_name = input("What can I get for you? ").strip().lower()
        if item_name not in menu:
            print("I'm sorry, we don't serve that. Try again.")
        else:
            quantity = int(input(f"How many {item_name}s would you like? ").strip())
            order.append([item_name, quantity])
            more = input("Anything else? yes/no: ").strip().lower()
            if more == 'no':
                return order


# print(get_order(menu))

# 3
array1 = np.random.randint(1, 101, 50)
array2 = np.random.randint(1, 101, 50)
print(array1, array2)
sum_arrays = array1 + array2
product_arrays = array1 * array2
division_arrays = array1 / array2
difference_arrays = array1 - array2

# print(sum_arrays, product_arrays, division_arrays, difference_arrays)

combined_array = np.concatenate((array1, array2))
reshaped_array = combined_array.reshape(5, 20)

print("Sum of arrays:\n", sum_arrays)
print("Product of arrays:\n", product_arrays)
print("Division of arrays:\n", division_arrays)
print("Difference of arrays:\n", difference_arrays)
print("Combined and reshaped array:\n", reshaped_array)


# 5
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 640)
        MainWindow.setStyleSheet("background-color: \"#ffe7ef\"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(230, 200, 281, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.product_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.product_label.setStyleSheet("background-color: #ffe7ef")
        self.product_label.setObjectName("product_label")
        self.horizontalLayout_2.addWidget(self.product_label)
        self.product_field = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.product_field.setStyleSheet("background-color: #ffffff")
        self.product_field.setObjectName("product_field")
        self.horizontalLayout_2.addWidget(self.product_field)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.increase_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.increase_button.setStyleSheet("background-color: #ffffff")
        self.increase_button.setObjectName("increase_button")
        self.horizontalLayout.addWidget(self.increase_button)
        self.change_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.change_button.setStyleSheet("background-color: #ffffff")
        self.change_button.setObjectName("change_button")
        self.horizontalLayout.addWidget(self.change_button)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.price_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.price_label.setStyleSheet("background-color: #ffe7ef")
        self.price_label.setObjectName("price_label")
        self.horizontalLayout_3.addWidget(self.price_label)
        self.price_field = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.price_field.setStyleSheet("background-color: #ffffff")
        self.price_field.setObjectName("price_field")
        self.horizontalLayout_3.addWidget(self.price_field)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.message_label = QtWidgets.QLabel(self.centralwidget)
        self.message_label.setGeometry(QtCore.QRect(0, 500, 770, 100))
        self.message_label.setStyleSheet("background-color: #ffffff; border: 1px solid black;")
        self.message_label.setAlignment(QtCore.Qt.AlignTop)
        self.message_label.setObjectName("message_label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.increase_button.clicked.connect(self.increase_price)
        self.change_button.clicked.connect(self.change_price)

        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["menuDB"]
        self.collection = self.db["menu"]
        self.init_menu()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.product_label.setText(_translate("MainWindow", "Product"))
        self.increase_button.setText(_translate("MainWindow", "Increase"))
        self.change_button.setText(_translate("MainWindow", "Change"))
        self.price_label.setText(_translate("MainWindow", "Price"))

    def init_menu(self):
        menu_dict = {"soda": 5.2, "wine": 5.6, "burger": 1.99, "tea": 2.5, "milk": 2.4, "chicken": 4.1}
        for item, price in menu_dict.items():
            self.collection.update_one({"item": item}, {"$set": {"price": price}}, upsert=True)

    def increase_price(self):
        item = self.product_field.text()
        if item:
            result = self.collection.update_one({"item": item}, {"$inc": {"price": 1}})
            if result.matched_count:
                self.display_message(f"Price of {item} increased by 1.")
            else:
                self.display_message(f"{item} not found.")
        else:
            self.display_message("Enter a product name.")
        self.display_menu()

    def change_price(self):
        item = self.product_field.text()
        try:
            price = float(self.price_field.text())
            self.collection.update_one({"item": item}, {"$set": {"price": price}}, upsert=True)
            self.display_menu()
        except ValueError:
            self.display_message("Enter a numeric value.")

    def display_menu(self):
        items = self.collection.find()
        menu_dict = {item['item']: item['price'] for item in items}
        self.display_message(str(menu_dict))

    def display_message(self, message):
        print(message)
        if len(message) > 95:
            split_index = message[:95].rfind(' ')
            message = message[:split_index] + '\n' + message[split_index + 1:]
        self.message_label.setText(message)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
