# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(382, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grp_login = QtWidgets.QGroupBox(self.centralwidget)
        self.grp_login.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.grp_login.setTitle("")
        self.grp_login.setObjectName("grp_login")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grp_login)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.grp_login)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_spTitle_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Meiryo")
        font.setPointSize(34)
        self.lbl_spTitle_2.setFont(font)
        self.lbl_spTitle_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_spTitle_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_spTitle_2.setObjectName("lbl_spTitle_2")
        self.horizontalLayout_2.addWidget(self.lbl_spTitle_2)
        self.btn_girisCik = QtWidgets.QPushButton(self.frame)
        self.btn_girisCik.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_girisCik.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_girisCik.setStyleSheet("QPushButton{\n"
"\n"
"color: #000;\n"
"border-radius:5px;\n"
"border-style:none;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 127);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 220, 220);\n"
"}")
        self.btn_girisCik.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-x-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_girisCik.setIcon(icon1)
        self.btn_girisCik.setObjectName("btn_girisCik")
        self.horizontalLayout_2.addWidget(self.btn_girisCik)
        self.verticalLayout.addWidget(self.frame)
        self.label = QtWidgets.QLabel(self.grp_login)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.txt_kullaniciadi = QtWidgets.QLineEdit(self.grp_login)
        self.txt_kullaniciadi.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"border-bottom: 1px solid rgb(44, 49, 60);\n"
"gridline-color: rgb(44, 49, 60);\n"
"color: rgb(255, 255, 255);")
        self.txt_kullaniciadi.setObjectName("txt_kullaniciadi")
        self.verticalLayout.addWidget(self.txt_kullaniciadi)
        self.label_2 = QtWidgets.QLabel(self.grp_login)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.txt_sifre = QtWidgets.QLineEdit(self.grp_login)
        self.txt_sifre.setStyleSheet("background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    gridline-color: rgb(44, 49, 60);\n"
"color: rgb(255, 255, 255);")
        self.txt_sifre.setObjectName("txt_sifre")
        self.verticalLayout.addWidget(self.txt_sifre)
        self.label_3 = QtWidgets.QLabel(self.grp_login)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.cmb_giris_tipi = QtWidgets.QComboBox(self.grp_login)
        self.cmb_giris_tipi.setStyleSheet("QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(85, 170, 255);    \n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.cmb_giris_tipi.setObjectName("cmb_giris_tipi")
        self.cmb_giris_tipi.addItem("")
        self.cmb_giris_tipi.addItem("")
        self.verticalLayout.addWidget(self.cmb_giris_tipi)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.btn_girisyap = QtWidgets.QPushButton(self.grp_login)
        self.btn_girisyap.setMaximumSize(QtCore.QSize(150, 35))
        self.btn_girisyap.setStyleSheet("QPushButton{\n"
"background-color: rgb(197, 197, 197);\n"
"color: #000;\n"
"border-radius:5px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 127);\n"
"\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 220, 220);\n"
"}")
        self.btn_girisyap.setObjectName("btn_girisyap")
        self.verticalLayout.addWidget(self.btn_girisyap)
        self.lbl_invalid = QtWidgets.QLabel(self.grp_login)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(9)
        self.lbl_invalid.setFont(font)
        self.lbl_invalid.setObjectName("lbl_invalid")
        self.verticalLayout.addWidget(self.lbl_invalid)
        self.btn_sifreDegis = QtWidgets.QPushButton(self.grp_login)
        self.btn_sifreDegis.setMinimumSize(QtCore.QSize(150, 0))
        self.btn_sifreDegis.setMaximumSize(QtCore.QSize(150, 16777215))
        self.btn_sifreDegis.setStyleSheet("QPushButton{\n"
"border-style:none;\n"
"color: rgb(255, 255, 255);\n"
"text-align:left;\n"
"}\n"
"QPushButton::hover{\n"
"color:rgb(85, 85, 255);\n"
"}")
        self.btn_sifreDegis.setObjectName("btn_sifreDegis")
        self.verticalLayout.addWidget(self.btn_sifreDegis)
        self.horizontalLayout.addWidget(self.grp_login)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login Sayfası"))
        self.lbl_spTitle_2.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-style:italic;\">HOGG</span><span style=\" vertical-align:sub;\"/><span style=\" font-weight:600; vertical-align:sub;\">PANEL</span></p></body></html>"))
        self.label.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#fafafa;\">Email Adresi</span></p></body></html>"))
        self.label_2.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#fefefe;\">Şifre</span></p></body></html>"))
        self.label_3.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#ffffff;\">Kullanıcı Şekli:</span></p></body></html>"))
        self.cmb_giris_tipi.setItemText(0, _translate("LoginWindow", "Admin Girişi"))
        self.cmb_giris_tipi.setItemText(1, _translate("LoginWindow", "Personel Girişi"))
        self.btn_girisyap.setText(_translate("LoginWindow", "Giriş Yap"))
        self.lbl_invalid.setText(_translate("LoginWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Kullanıcı adı veya parola Yanlış!</span></p></body></html>"))
        self.btn_sifreDegis.setText(_translate("LoginWindow", "Şifreni mi unuttun ?"))
import files_rc