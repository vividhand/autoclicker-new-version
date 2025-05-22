import PyQt6
from PyQt6 import QtCore, QtGui, QtWidgets
import pynput
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller, Listener, Key
import time
import threading
import sys

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.key_dict = {
            # Специальные клавиши (Key)
            "esc": Key.esc,
            "f1": Key.f1,
            "f2": Key.f2,
            "f3": Key.f3,
            "f4": Key.f4,
            "f5": Key.f5,
            "f6": Key.f6,
            "f7": Key.f7,
            "f8": Key.f8,
            "f9": Key.f9,
            "f10": Key.f10,
            "f11": Key.f11,
            "f12": Key.f12,

            "tab": Key.tab,
            "caps_lock": Key.caps_lock,
            "shift": Key.shift,
            "shift_r": Key.shift_r,
            "ctrl": Key.ctrl,
            "ctrl_r": Key.ctrl_r,
            "alt": Key.alt,
            "alt_r": Key.alt_r,
            "cmd": Key.cmd,
            "cmd_r": Key.cmd_r,

            "space": Key.space,
            "enter": Key.enter,
            "backspace": Key.backspace,
            "delete": Key.delete,
            "insert": Key.insert,

            "home": Key.home,
            "end": Key.end,
            "page_up": Key.page_up,
            "page_down": Key.page_down,

            "up": Key.up,
            "down": Key.down,
            "left": Key.left,
            "right": Key.right,

            "num_lock": Key.num_lock,
            "scroll_lock": Key.scroll_lock,
            "pause": Key.pause,
            "print_screen": Key.print_screen,

            "menu": Key.menu,

            # Мультимедиа
            "media_play_pause": Key.media_play_pause,
            "media_volume_mute": Key.media_volume_mute,
            "media_volume_down": Key.media_volume_down,
            "media_volume_up": Key.media_volume_up,
            "media_previous": Key.media_previous,
            "media_next": Key.media_next,
        }
        self.mouse = pynput.mouse.Controller()
        self.keyboard = pynput.keyboard.Controller()
        self.status = "Stop"             #Остановлен по умолчанию
        self.click_button = "ЛКМ"        #Лкм по умолчанию
        self.choose_hotkey = Key.f8             #F8 по умолчанию
        self.information = "Горячая клавиша по умолчанию f8"

        self.setObjectName("Autoclicker")
        self.setEnabled(True)
        self.resize(400, 300)
        self.setStyleSheet("")

        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)

        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.tabWidget.setStyleSheet("border-radius: 20px")
        self.tabWidget.setObjectName("tabWidget")

        # Tab 3 (Файл)
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.label_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.tab_3)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_exit = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.btn_exit.setStyleSheet(
            "border: 3px solid rgba(0, 0, 0, 1);\nfont: 36pt \"Segoe UI\";\n"
        )
        self.btn_exit.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.btn_exit, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "Файл")

        # Tab 1 (Autoclicker)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(parent=self.tab)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_status = QtWidgets.QLabel(parent=self.tab)
        self.label_status.setGeometry(QtCore.QRect(240, 10, 150, 50))
        self.label_status.setStyleSheet("border: 2px solid rgba(0, 0, 0, 1);\nborder-radius: 20px")
        self.label_status.setObjectName("label_2")
        self.btn_start = QtWidgets.QPushButton(parent=self.tab)
        self.btn_start.setGeometry(QtCore.QRect(20, 60, 100, 60))
        self.btn_start.setStyleSheet(
            "background-color: rgba(170, 170, 255, 150);\n"
            "border-radius: 15px;\n"
            "font: 600 14pt \"Segoe UI\";"
        )
        self.btn_start.setObjectName("pushButton")
        self.btn_stop = QtWidgets.QPushButton(parent=self.tab)
        self.btn_stop.setGeometry(QtCore.QRect(20, 180, 100, 60))
        self.btn_stop.setStyleSheet(
            "background-color: rgba(170, 170, 255, 150);\n"
            "border-radius: 15px;\n"
            "font: 600 14pt \"Segoe UI\";"
        )
        self.btn_stop.setObjectName("pushButton_2")
        self.label_information_1 = QtWidgets.QLabel(parent=self.tab)
        self.label_information_1.setGeometry(QtCore.QRect(150, 70, 241, 101))
        self.label_information_1.setStyleSheet("border: 3px solid rgba(0, 0, 0, 1);")
        self.label_information_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_information_1.setObjectName("label_7")
        self.tabWidget.addTab(self.tab, "Autoclicker")

        # Tab 2 (Setting)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.radioButton_LKM = QtWidgets.QRadioButton(parent=self.tab_2)
        self.radioButton_LKM.setGeometry(QtCore.QRect(330, 50, 50, 20))
        self.radioButton_LKM.setObjectName("radioButton")
        self.radioButton_PKM = QtWidgets.QRadioButton(parent=self.tab_2)
        self.radioButton_PKM.setGeometry(QtCore.QRect(330, 100, 50, 20))
        self.radioButton_PKM.setObjectName("radioButton_2")
        self.radioButton_SKM = QtWidgets.QRadioButton(parent=self.tab_2)
        self.radioButton_SKM.setGeometry(QtCore.QRect(330, 150, 50, 20))
        self.radioButton_SKM.setObjectName("radioButton_3")
        self.label_speed = QtWidgets.QLabel(parent=self.tab_2)
        self.label_speed.setGeometry(QtCore.QRect(0, 10, 165, 40))
        self.label_speed.setStyleSheet("border: 2px solid rgba(0, 0, 0, 1);")
        self.label_speed.setObjectName("label_4")
        self.lineEdit_speed = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_speed.setGeometry(QtCore.QRect(32, 50, 100, 30))
        self.lineEdit_speed.setStyleSheet("border: 2px solid rgba(0, 0, 0, 1);")
        self.lineEdit_speed.setObjectName("lineEdit")
        self.label_hotkey = QtWidgets.QLabel(parent=self.tab_2)
        self.label_hotkey.setGeometry(QtCore.QRect(0, 100, 170, 40))
        self.label_hotkey.setStyleSheet("border: 2px solid rgba(0, 0, 0, 1);")
        self.label_hotkey.setObjectName("label_5")
        self.lineEdit_hotkey = QtWidgets.QLineEdit(parent=self.tab_2)
        self.lineEdit_hotkey.setGeometry(QtCore.QRect(35, 140, 100, 30))
        self.lineEdit_hotkey.setStyleSheet("border: 2px solid rgba(0, 0, 0, 1);")
        self.lineEdit_hotkey.setObjectName("lineEdit_2")
        self.label_information_2= QtWidgets.QLabel(parent=self.tab_2)
        self.label_information_2.setGeometry(QtCore.QRect(150, 170, 241, 101))
        self.label_information_2.setStyleSheet("border: 3px solid rgba(0, 0, 0, 1);")
        self.label_information_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_information_2.setObjectName("label_6")
        self.tabWidget.addTab(self.tab_2, "Setting")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.radioButton_LKM.toggled.connect(self.radio_button)
        self.radioButton_PKM.toggled.connect(self.radio_button)
        self.radioButton_SKM.toggled.connect(self.radio_button)
        self.click_start()
        self.click_stop()
        self.listener_thread = threading.Thread(target=self.clicking_listener, daemon=True).start()
        self.radio_button()
        self.hotkey()
        self.lineEdit_hotkey.textChanged.connect(self.hotkey)
        self.exit()
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Autoclicker"))
        self.btn_exit.setText(_translate("MainWindow", "Выйти"))
        self.label_status.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Status</span><span style=\" font-size:14pt;\">: </span><span style=\" font-size:14pt; font-weight:700; color:#ff0000;\">STOPED</span></p></body></html>"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.label_information_1.setText(_translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:11pt;\">Информативное окно:</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; font-style:italic;\">Горячая клавиша</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; font-style:italic; text-decoration: underline;\">&quot;F8&quot;</span></p></body></html>"))
        self.radioButton_LKM.setText(_translate("MainWindow", "ЛКМ"))
        self.radioButton_PKM.setText(_translate("MainWindow", "ПКМ"))
        self.radioButton_SKM.setText(_translate("MainWindow", "СКП"))
        self.label_speed.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Задержка 'сек' </span></p></body></html>"))
        self.label_hotkey.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Горячая клавиша</span></p></body></html>"))
        self.label_information_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Информативное окно:</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; font-style:italic;\">Горячая клавиша</span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; font-style:italic;\">по умолчанию </span><span style=\" font-size:11pt; font-weight:700; font-style:italic; text-decoration: underline;\">&quot;F8&quot;</span></p></body></html>"))


    def click_start(self):
        self.btn_start.clicked.connect(self.start_clicker)

    def click_stop(self):
        self.btn_stop.clicked.connect(self.stop_clicker)


    def start_clicker(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_status.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Status</span><span style=\" font-size:14pt;\">: </span><span style=\" font-size:14pt; font-weight:700; color:#ff74ff00;\">START</span></p></body></html>"))

        self.status = "Start"
        print(self.status)
        threading.Thread(target=self.clicking, daemon=True).start()

    def stop_clicker(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_status.setText(_translate("MainWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-style:italic;\">Status</span><span style=\" font-size:14pt;\">: </span><span style=\" font-size:14pt; font-weight:700; color:#ff0000;\">STOPED</span></p></body></html>"))
        self.status = "Stop"
        print(self.status)

    def clicking(self):
        try:
            time.sleep(1)
            while self.status == "Start":
                if self.click_button == "ЛКМ":
                    self.mouse.click(Button.left)
                elif self.click_button == "ПКМ":
                    self.mouse.click(Button.right)
                elif self.click_button == "СКМ":
                    self.mouse.click(Button.middle)

                time.sleep(self.data_speed())
        except  Exception as e:
            self.information = e


    def clicking_listener(self):
        with Listener(on_press=self.on_key_press) as listener:
            listener.join()

    def on_key_press(self, key):
        if self.status == "Start" and key == self.choose_hotkey:
            self.stop_clicker()
        elif self.status == "Stop" and key == self.choose_hotkey:
            self.start_clicker()

    def radio_button(self):
        if self.radioButton_LKM.isChecked():
            self.click_button = "ЛКМ"
        elif self.radioButton_PKM.isChecked():
            self.click_button = "ПКМ"
        elif self.radioButton_SKM.isChecked():
            self.click_button = "СКМ"

    def hotkey(self):
        key_name = self.lineEdit_hotkey.text()
        if key_name in self.key_dict:
            self.choose_hotkey = self.key_dict[key_name]
        else:
            self.choose_hotkey = Key.f8  # значение по умолчанию

    def data_speed(self):
        try:
            return float(self.lineEdit_speed.text())
        except ValueError:
            return 0.01  # значение по умолчанию

    def exit(self):
        self.btn_exit.clicked.connect(self.exited)

    def exited(self):
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_MainWindow()
    window.show()
    sys.exit(app.exec())