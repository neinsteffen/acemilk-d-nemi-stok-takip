
from PyQt5 import QtWidgets, QtCore, QtGui
from Ui_Login import Ui_LoginWindow
from anasayfa import AnaSayfa
import pyrebase
api = "AIzaSyAa8fsFTUo_H6e7mHv4DIEzH78Bcb5mZvc"

class Giris(QtWidgets.QMainWindow):
    def __init__(self):
        super(Giris, self).__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.anasayfa = AnaSayfa()
        #degisken kodları
        self.ui.btn_girisCik.clicked.connect(self.cikisyap)
        self.ui.btn_girisyap.clicked.connect(self.girisyap)
        self.ui.btn_sifreDegis.clicked.connect(self.sifreDegis)
        #köşeleri kaldır
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.lbl_invalid.setVisible(False)
        ##veritabanı bağlantı
        self.Config = {
            "apiKey": api,
            "authDomain": "magaza-de6af.firebaseapp.com",
            "projectId": "magaza-de6af",
            "databaseURL": "magaza-de6af-default-rtdb.europe-west1.firebasedatabase.app",
            "storageBucket": "magaza-de6af.appspot.com",
            "messagingSenderId": "1099255267210",
            "appId": "1:1099255267210:web:d47e6426eeeae1779d1273",
            "measurementId": "G-C76Z82E20N"
        }
        self.firebase = pyrebase.initialize_app(self.Config)
        self.auth = self.firebase.auth()
        

    #giriş işlemlerinin yönetildiği yer
    def girisyap(self):
        """
        burası giriş yap dedikten sonra firestore ve login işlemlerinin kontrol edildiği yer
        """
        
        
        sifre=self.ui.txt_sifre.text()
        email=self.ui.txt_kullaniciadi.text()

        try:
            login = self.auth.sign_in_with_email_and_password(email,sifre)
            self.anasayfa.show()
            self.close()
        except Exception as e:
            print("Hata oldu. Kod: ",e)
            self.ui.lbl_invalid.setVisible(True)
            self.ui.lbl_invalid.setText("Kullanıcı adı veya şifre yanlış")
            self.ui.lbl_invalid.setStyleSheet('color:#900;')

      
        
    def cikisyap(self):
        """
        burası çıkış yapılmasını sağlayacak bölüm
        """
        self.close()
    def sifreDegis(self):
        
       
        if self.ui.txt_kullaniciadi.text()=="":
            email=self.ui.txt_kullaniciadi.text()
            self.ui.lbl_invalid.setText("Email adresini yukarı gir")
            self.ui.lbl_invalid.setStyleSheet('color:#900;')
            self.ui.lbl_invalid.setVisible(True)
        else:
            email=self.ui.txt_kullaniciadi.text()
            self.auth.send_password_reset_email(email)
            self.ui.lbl_invalid.setText("Email adresini kontrol et")
            self.ui.lbl_invalid.setStyleSheet('color:#fff;')
            self.ui.lbl_invalid.setVisible(True)
           

        
        
        
        
        




